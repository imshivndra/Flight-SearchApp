from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import FlightDetailsSerializer
from .models import FlightDetails
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
def AddFlightDetails(request):
    serializer=FlightDetailsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201) 
    return JsonResponse(serializer.errors,status=400)

@api_view(['POST'])
def SearchFlight(request):
    departure_city=request.data.get("departure_city")
    arrival_city=request.data.get("arrival_city")
    search_time=request.data.get("departure_time")
    flightData=FlightDetails.objects.all()
    # for i in flightData:
    #     print(i.departure_city)
    # # print("details are ",serializer.data)
    # return JsonResponse(serializer.data,safe=False) 

# implementing search
    from collections import defaultdict

    class Graph():
     def __init__(self):
       
        self.edges = defaultdict(list)
        self.weights = {}

     def add_edge(self, id,from_node, to_node,departure_time,arrival_time):
        
        self.edges[from_node].append([to_node,id,departure_time,arrival_time])
       
       

    graph = Graph()

    edges=[]
    for element in flightData:
     edges.append((element.id,element.departure_city,element.arrival_city,element.departure_time,element.arrival_time))
    for edge in edges:
     graph.add_edge(*edge)
    def dijsktra(graph, initial, end,search_time):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
        shortest_paths = {initial: (None, 0,None,None,None)}
        current_node = initial
        visited = set()
  
        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]
            for next_node,id,departure_time,arrival_time in destinations:
                if search_time<=departure_time:              
                    weight = arrival_time-search_time + weight_to_current_node

                    if next_node not in shortest_paths:
                        shortest_paths[next_node] = (current_node, weight,id,departure_time,arrival_time)                      
                    else:
                        current_shortest_weight = shortest_paths[next_node][1]
                        if current_shortest_weight > weight:
                            shortest_paths[next_node] = (current_node, weight,id,departure_time,arrival_time)
            
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
            # Flights only after arrival on destination
            search_time=next_destinations[current_node][4]
        # Work back through destinations in shortest path
        path = []
        current_id=0
        while current_node is not None:
            next_node = shortest_paths[current_node][0]
            current_id=shortest_paths[current_node][2]
            path.append(current_id)
            current_node = next_node
        # Reverse path
        path = path[::-1]
        path=path[1:]
        return path
        # Method to get shortest flight id's
    flight_ids=(dijsktra(graph, departure_city,arrival_city,search_time))
    flights_information=[]
    for flight_id in flight_ids:
        for element in flightData:
            if element.id==flight_id:
                flights_information.append(element)
    serializer=FlightDetailsSerializer(flights_information,many=True )
    return JsonResponse(serializer.data,safe=False)



@api_view(['PUT'])
def UpdateFlightDetails(request,id):
    flightDetailsReturned=FlightDetails.objects.get(id=id)
    serializer=FlightDetailsSerializer(instance=flightDetailsReturned,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201) 
    return JsonResponse(serializer.errors,status=400)    

