"""Angus is attending the Christchurch Buskers Festival and wants to see as many
shows as he can on a given day. He has a list of all the shows in an arbitrary 
order. Each one is a tuple with a title, a start time 
(conveniently specified in minutes from the midnight) and a duration, also in minutes. Help Angus decide what shows to attend.

Write a function print_shows(show_list) that takes a list of show tuples as 
defined above and prints in order of start time the list of shows that Angus 
should attend, as obtained using the algorithm in the lecture notes. Shows are
printed one per line with the title, start and end times separated by a comma 
and a space as shown in the example. To ensure a unique solution, you may 
assume that show end times are unique."""

def print_shows(show_list):
    show_list.sort(key = lambda x: x[1] + x[2])
    S = []
    last = 0
    for j in range(len(show_list)):
        if show_list[j][1] >= last:
            last = (show_list[j][1] + show_list[j][2])
            S.append((show_list[j][0],show_list[j][1], last))
    for i in S:
        print('{}, {}, {}'.format(i[0], i[1], i[2]))

# The example from the lecture notes
print_shows([
    ('a', 0, 6),
    ('b', 1, 3),
    ('c', 3, 2),
    ('d', 3, 5),
    ('e', 4, 3),
    ('f', 5, 4),
    ('g', 6, 4), 
    ('h', 8, 3)])