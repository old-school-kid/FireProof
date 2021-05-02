from flask import Flask, render_template, url_for, redirect, request, flash
import numpy as np
import sys
import datetime
import json
import requests
import fire
import path
from collections import defaultdict

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/isfire', methods=['POST'])
def isfire():
    class Graph:
        
        def __init__(self): 
            self.ans = []
            
        def minDistance(self, dist,queue):
            minimum = float("Inf")
            min_index = -1
            
            for i in range(len(dist)):
                if dist[i] < minimum and i in queue:
                    minimum = dist[i]
                    min_index = i
            return min_index
       
        def dijkstra(self, graph, src):
            row = len(graph)
            col = len(graph[0])
            
            dist = [float("Inf")]*row
            
            parent = [-1]*row
            
            dist[src] = 0
            
            queue = []
            for i in range(row):
                queue.append(i)
                
            while queue:
                
                u = self.minDistance(dist, queue)
                queue.remove(u)
                
                for i in range(col):
                    if graph[u][i] and i in queue:
                        if dist[u] + graph[u][i] < dist[i]:
                            dist[i] = dist[u] + graph[u][i]
                            parent[i] = u
            for i in range(row):
                temp = []
                par = i 
                while par!=-1:
                    temp.append((par+1))
                    par = parent[par]
                self.ans.append(temp)
            return self.ans
        
    graph = [[0,1,1,1,0,0],
             [1,0,1,0,0,0],
             [1,1,0,1,0,1],
             [1,0,1,0,1,0],
             [0,0,0,1,0,1],
             [0,0,1,0,1,0]]   
    
    flag = False
    temparr = np.zeros(6)
    for i in range(6):
        file = request.files[str(i+1)]
        res = fire.fire("images/" + file.filename)
        temparr[i] = res
        flag = flag or res

    if not flag:
        return "You are safe!"
    
    for i in range(6):
        for j in range(6):
            if graph[i][j]!=0 :
                val = (temparr[i]+temparr[j])/2+1
                graph[i][j]=graph[j][i]=val
    
    g= Graph()
    
    final_path = g.dijkstra(graph,0)
    return render_template('index.html', final_path=final_path)


if __name__=="__main__":
    app.run(port=5000, debug=True)