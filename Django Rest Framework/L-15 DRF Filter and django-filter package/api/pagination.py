from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

# Custom Pagination for local classes
class PageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    # client define pagination or How many records will be shown in each page
    page_size_query_param = 'records'
    
    '''
    http://127.0.0.1:8000/studentapi/?p=2&records=10
    '''
    max_page_size = 7
    '''
    http://127.0.0.1:8000/studentapi/?p=last --> go to the last page
    http://127.0.0.1:8000/studentapi/?p=end --> changing from last to end
    '''
    last_page_strings = 'end'
    



class PageLimitOffsetPagination(LimitOffsetPagination):
    """
    this pagination is used for giving the client facility to start from a specific number and set a specific limit per page
    http://127.0.0.1:8000/studentapi/?limit=4&offset=4 -->default settings for locla usage we can aslo set global settings
    """
    # Records per page
    default_limit = 5
    # Custom name for limit, which will be passed through url
    limit_query_param = 'mylimit'
    # Custom name for starting records
    offset_query_param = 'myoffset'
    '''
    http://127.0.0.1:8000/studentapi/?mylimit=5&myoffset=15 --> new url pattern after customizing query_param
    '''
    max_limit = 6
    

class MyCursorPagination(CursorPagination):
    '''
    this pagination is only used for next and previous pagination 
    This also support ordering
    This one is used fro showing latest data first
    By default it uses timestamp for ordering. If timestamp is not define into our model, we have to use
    other fields for ordering.
    '''
    page_size = 10
    ordering = 'name'
    
    # http://127.0.0.1:8000/studentapi/?cursor=cD1SaXphbg%3D%3D --> default query name
    # http://127.0.0.1:8000/studentapi/?mycursor=cD1SaXphbg%3D%3D --> customize query name
    cursor_query_param = 'mycursor'
    