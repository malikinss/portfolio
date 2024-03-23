# ["1:[5]", "4:[5]", "3:[5]", "5:[1,4,3,2]", "2:[5,15,7]", "7:[2,8]", "8:[7,38]", "15:[2]", "38:[8]"]

def get_neighbour_points(city_record):
  neighbours = city_record[(city_record.find(":") + 2):-1]
  neighbours = neighbours.split(',')

  return list(map(int, neighbours))

def get_current_point(point_record):
  # "POINT:[VALUES]"
  current_point = int(point_record[:point_record.find(":")])

  return current_point

def get_cities_db(strArr):
  cities_db = {}

  for city_record in strArr:
    current_city = get_current_point(city_record)
    neighbours = get_neighbour_points(city_record)

    if current_city not in cities_db.keys():
      cities_db[current_city] = neighbours

  return cities_db

def get_next_points(cities_db, traveled_path, current_point):
  next_possible_points = cities_db.get(current_point)
  next_points = []

  for point in next_possible_points:
    if point not in traveled_path:
      next_points.append(point)
  
  return next_points  

def display_path(given_path, next_points):
  print(given_path, next_points, sep='-')

def is_empty(any_list):
  return len(any_list) == 0  

def update_all_possible_paths(all_possible_paths, next_points, traveled_path):
  if is_empty(next_points):
    all_possible_paths.append(traveled_path.copy())

  return all_possible_paths

def get_edge_nodes(cities_db):
  edge_nodes = []

  for node, paths in cities_db.items():
    if len(paths) == 1:
      edge_nodes.append(node)

  return edge_nodes

cities_db = get_cities_db(input())
edge_nodes = get_edge_nodes(cities_db)

#print(edge_nodes)

all_possible_paths = []
traveled_path = []

next_points = cities_db.keys() 

for point in next_points:
  traveled_path.append(point)
  next_points = get_next_points(cities_db, traveled_path, point)
  all_possible_paths = update_all_possible_paths(all_possible_paths, next_points, traveled_path)

  display_path(traveled_path, next_points) #
  traveled_path.remove(point)

print()
print(all_possible_paths)

def CityTraffic(strArr):

  return strArr

# keep this function call here 
#print(CityTraffic(input()))
