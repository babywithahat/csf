# Name: Alejandro Chavez 
# Evergreen Login: chaveza 
# Programming as a Way of Life
# Homework 5: Election prediction

import csv
import os
import time
import math

def read_csv(path):
    """
    Reads the CSV file at path, and returns a list of rows. Each row is a
    dictionary that maps a column name to a value in that column, as a string.
    """
    output = []
    for row in csv.DictReader(open(path)):
        output.append(row)
    return output


################################################################################
# Problem 1: State edges
################################################################################

def row_to_edge(row):
    """
    Given an election result row or poll data row, returns the Democratic edge
    in that state.
    """
    return float(row["Dem"]) - float(row["Rep"])  

def state_edges(election_result_rows):
    """
    Given a list of election result rows, returns state edges.
    The input list does has no duplicate states;
    that is, each state is represented at most once in the input list.
    """
    state_edges_values = {}
    for row in election_result_rows:
      state_edges_values[row['State']] = row_to_edge(row)
    return state_edges_values



################################################################################
# Problem 2: Find the most recent poll row
################################################################################

def earlier_date(date1, date2):
    """
    Given two dates as strings (formatted like "Oct 06 2012"), returns True if 
    date1 is after date2.
    """
    return (time.strptime(date1, "%b %d %Y") < time.strptime(date2, "%b %d %Y"))

def most_recent_poll_row(poll_rows, pollster, state):
    """
    Given a list of poll data rows, returns the most recent row with the
    specified pollster and state. If no such row exists, returns None.
    """
    return_row = {}
    relavent_rows = []
    for row in poll_rows:
      if (row['Pollster']==pollster and row['State']==state):
        relavent_rows.append(row)
    if (len(relavent_rows) > 1):
      return_row = relavent_rows[0]
      for a in range(0, (len(relavent_rows)-1)):
        if earlier_date(return_row['Date'], relavent_rows[a+1]['Date']):
          return_row=relavent_rows[a+1]
    elif (len(relavent_rows) == 1):
      return relavent_rows[0]
    else:
      return None
    return return_row


################################################################################
# Problem 3: Pollster predictions
################################################################################


def tuple_date_sort(date_tuple):
    date_list = list(date_tuple)
    

def unique_column_values(rows, column_name):
    """
    Given a list of rows and the name of a column (a string), returns a set
    containing all values in that column.
    """
    return_set = set()
    for row in rows:
      if (row[column_name] not in return_set):
        return_set.add(row[column_name])
    return set(return_set)

def poll_column_row_match(poll_rows, column, value):
    return_rows = []
    for row in poll_rows:
      if row[column]==value:
        return_rows.append(row)
    return return_rows

def pollster_predictions(poll_rows):
    """
    Given a list of poll data rows, returns pollster predictions.
    """
    predictions = {}
    states_with_pollster = {}
    
    pollsters = unique_column_values(poll_rows, 'Pollster')
    for poll_id in pollsters:
      most_recent_polls={}
      states_with_pollster[poll_id] = poll_column_row_match(poll_rows, 'Pollster', poll_id)
      states = unique_column_values(states_with_pollster[poll_id], 'State')
      for state in states:
        most_recent_polls[state]= most_recent_poll_row(states_with_pollster[poll_id], poll_id, state)
      predictions[poll_id] = state_edges(most_recent_polls.values())
    return predictions 

            
################################################################################
# Problem 4: Pollster errors
################################################################################

def average_error(state_edges_predicted, state_edges_actual):
    """
    Given predicted state edges and actual state edges, returns
    the average error of the prediction.
    """
    valid_states = []
    nums = []
    for state in state_edges_predicted:
        if state in state_edges_actual:
          nums.append(math.fabs(state_edges_predicted[state]-state_edges_actual[state]))
          valid_states.append(state)
    sum = 0
    for k in nums:
      sum += k
    average = sum/len(nums)
    return average

def pollster_errors(pollster_predictions, state_edges_actual):
    return_errors = {}
    for polls in pollster_predictions:
      return_errors[polls]= average_error(pollster_predictions[polls], state_edges_actual)
    return return_errors
    """
    Given pollster predictions and actual state edges, retuns pollster errors.
    """
    #TODO: Implement this function
    pass


################################################################################
# Problem 5: Pivot a nested dictionary
################################################################################

def pivot_nested_dict(nested_dict):
    """
    Pivots a nested dictionary, producing a different nested dictionary
    containing the same values.
    The input is a dictionary d1 that maps from keys k1 to dictionaries d2,
    where d2 maps from keys k2 to values v.
    The output is a dictionary d3 that maps from keys k2 to dictionaries d4,
    where d4 maps from keys k1 to values v.
    For example:
      input = { "a" : { "x": 1, "y": 2 },
                "b" : { "x": 3, "z": 4 } }
      output = {'y': {'a': 2},
                'x': {'a': 1, 'b': 3},
                'z': {'b': 4} }
    """
    return_dict = {}
    for key in nested_dict:
      for inner in nested_dict[key]:
        if inner not in return_dict:
          return_dict[inner]=1
    for key in return_dict:
      inner_dict={}
      for k in nested_dict:
        if key in nested_dict[k]:
          if k not in inner_dict:
            inner_dict[k]=nested_dict[k][key]
      return_dict[key]=inner_dict
    return return_dict

    print return_dict
    pass


################################################################################
# Problem 6: Average the edges in a single state
################################################################################

def average_error_to_weight(error):
    """
    Given the average error of a pollster, returns that pollster's weight.
    The error must be a positive number.
    """
    return error ** (-2)

# The default average error of a pollster who did no polling in the
# previous election.
DEFAULT_AVERAGE_ERROR = 5.0

def pollster_to_weight(pollster, pollster_errors):
    """"
    Given a pollster and a pollster errors, return the given pollster's weight.
    """
    if pollster not in pollster_errors:
        weight = average_error_to_weight(DEFAULT_AVERAGE_ERROR)
    else:
        weight = average_error_to_weight(pollster_errors[pollster])
    return weight


def weighted_average(items, weights):
    """
    Returns the weighted average of a list of items.
    
    Arguments:
    items is a list of numbers.
    weights is a list of numbers, whose sum is nonzero.
    
    Each weight in weights corresponds to the item in items at the same index.
    items and weights must be the same length.
    """
    assert len(items) > 0
    assert len(items) == len(weights)
    numerator = []
    for k in range(0, len(items)):
      numerator.append(items[k]*weights[k])
    return sum(numerator)/float(sum(weights))


def average_edge(pollster_edges, pollster_errors):
    """
    Given pollster edges and pollster errors, returns the average of these edges
    weighted by their respective pollster errors.
    """
    edges = []
    error = []
    for k in pollster_edges:
      edges.append(pollster_to_weight(k, pollster_edges))
    for k in pollster_errors:
      error.append(pollster_to_weight(k, pollster_errors))
    print sum(edges)
    print sum(error)
    pass

    
################################################################################
# Problem 7: Predict the 2012 election
################################################################################

def predict_state_edges(pollster_predictions, pollster_errors):
    """
    Given pollster predictions from a current election and pollster errors from
    a past election, returns the predicted state edges of the current election.
    """
    #TODO: Implement this function
    pass
    

################################################################################
# Electoral College, Main Function, etc.
################################################################################

def electoral_college_outcome(ec_rows, state_edges):
    """
    Given electoral college rows and state edges, returns the outcome of
    the Electoral College, as a map from "Dem" or "Rep" to a number of
    electoral votes won.  If a state has an edge of exactly 0.0, its votes
    are evenly divided between both parties.
    """
    ec_votes = {}               # maps from state to number of electoral votes
    for row in ec_rows:
        ec_votes[row["State"]] = float(row["Electors"])

    outcome = {"Dem": 0, "Rep": 0}
    for state in state_edges:
        votes = ec_votes[state]
        if state_edges[state] > 0:
            outcome["Dem"] += votes
        elif state_edges[state] < 0:
            outcome["Rep"] += votes
        else:
            outcome["Dem"] += votes/2.0
            outcome["Rep"] += votes/2.0
    return outcome


def print_dict(dictionary):
    """
    Given a dictionary, prints its contents in sorted order by key.
    Rounds float values to 8 decimal places.
    """
    for key in sorted(dictionary.keys()):
        value = dictionary[key]
        if type(value) == float:
            value = round(value, 8)
        print key, value


def main():
    """
    Main function, which is executed when election.py is run as a Python script.
    """
    # Read state edges from the 2008 election
    edges_2008 = state_edges(read_csv("data/2008-results.csv"))
    
    # Read pollster predictions from the 2008 and 2012 election
    polls_2008 = pollster_predictions(read_csv("data/2008-polls.csv"))
    polls_2012 = pollster_predictions(read_csv("data/2012-polls.csv"))
    
    # Compute pollster errors for the 2008 election
    error_2008 = pollster_errors(polls_2008, edges_2008)
    
    # Predict the 2012 state edges
    prediction_2012 = predict_state_edges(polls_2012, error_2008)
    
    # Obtain the 2012 Electoral College outcome
    ec_2012 = electoral_college_outcome(read_csv("data/2012-electoral-college.csv"),
                                        prediction_2012)
    
    print "Predicted 2012 election results:"
    print_dict(prediction_2012)
    print
    
    print "Predicted 2012 Electoral College outcome:"
    print_dict(ec_2012)
    print    


# If this file, election.py, is run as a Python script (such as by typing
# "python election.py" at the command shell), then run the main() function.
if __name__ == "__main__":
    main()
