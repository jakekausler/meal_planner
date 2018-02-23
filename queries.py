
import datetime


def GetCalendar(cursor, params):
    startDate = None
    endDate = None
    limit = -1
    page = 0
    if 'startdate' in params:
        startDate = datetime.datetime.strptime(params['startdate'][0], '%Y-%m-%dT%H:%M:%S.%fZ')
    if 'enddate' in params:
        endDate = datetime.datetime.strptime(params['enddate'][0], '%Y-%m-%dT%H:%M:%S.%fZ')
    query = "SELECT * FROM calendar"
    addedAnything = False
    if startDate:
        if addedAnything:
            query += " AND"
        else:
            query += " WHERE"
        query += " date >= '{}'".format(startDate)
        addedAnything = True
    if endDate:
        if addedAnything:
            query += " AND"
        else:
            query += " WHERE"
        query += " date <= '{}'".format(endDate)
        addedAnything = True
    cursor.execute(query)
    return cursor.fetchall()

def GetIngredients(cursor, params):
    query = "SELECT * FROM ingredients"
    cursor.execute(query)
    return cursor.fetchall()

def GetUnits(cursor, params):
    query = "SELECT * FROM units"
    cursor.execute(query)
    return cursor.fetchall()

def GetRecipes(cursor, params):
    query = "SELECT * FROM recipes"
    cursor.execute(query)
    return cursor.fetchall()
