<!-- Querying database -->
<!-- sql => structure query language -->
inserr => adding new record
update
delete
select => SELECT * FROM database_name

all = []

<!-- flsk-sqlalchemy methods -->
all => to get all records
filter
filter_by
delete
order_by
get
update
add

<!-- db instance  -->
session
add => dding new record
commit

<!-- class Post:
   def __init__(self, post_title, post_content, id=none):
       self.post_title = post_title
       self.post_content = post_content
       self.id = id

post1 = Post('Travel', 'The Dubai trip was interesting') -->

serialize our data => formating our data so that it can be transfered over the internet
json =>dta format that makes it easy to be transfered over the internet 

[<Post 1>] => we can not transfer this over the internet, what will do is to convert it into a dictionary 
(serialize) then convert it into a json object

flask sqlalchemy  relationship => one-to-many, one-to-one, many-to-many
seed our db
create our firat endpoint(API)

{
    "id":1,
    "post_title":"weather"
    "post_content":"It's rainy today"
}

<!-- SerializeMixin -->
to_dict()
