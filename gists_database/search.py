from .models import Gist

def search_gists(db_connection, **kwargs):
    
    if not kwargs:
        query = 'SELECT * from gists'
    elif 'github_id' in kwargs:
        query = 'SELECT * from gists WHERE github_id = :github_id'
    elif 'created_at' in kwargs:
        query = 'SELECT * from gists WHERE datetime(created_at) = datetime(:created_at)'
    
    cursor = db_connection.execute(query, kwargs)
    result = []
    for gist in cursor:
        result.append(Gist(gist))
    
    return result