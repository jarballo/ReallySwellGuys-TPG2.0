import pandas as pd
import mapper

data = mapper.Mapper()
customers = data.unique_customers

route_names = ['route1', 'route2', 'route3', 'route4', 'route5',
               'route6', 'route7', 'route8', 'route9', 'route10',
               'route11', 'route12', 'route13', 'route14']

columns = ['Company Number', 'Route Number', 'Date Serviced', 'Route Type',
           'Truck Number', 'Print Seq', 'Perm Seq', 'Lift Time', 'Account #',
           'Site', 'Container Group', 'Cont Qty', 'Cont Type', 'Container Size',
           'Site Name', 'Site Address #/Name', 'Site Address Line 2',
           'Site Suite #', 'City', 'State', 'Zip', 'Longitude', 'Latitude']
routes = []
for name in route_names:
    routes.append((data.get_entry(name), name))

for route, name in routes:
    # google lat and long aren't here yet
    route = route[columns]
    print(route.columns)
    a = route.merge(customers[['Site Address #/Name', 'google_lat',
                           'google_lng']],
                on='Site Address #/Name', how='left', suffixes=('',''))
    data.update_entry(a, name)

