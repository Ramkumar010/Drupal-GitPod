def football(scorecard):
    Total_points=0
    for i in scorecard:
        x=i.split(":")
        if x[0]>x[1]:
            Total_points=Total_points+3
        if x[0]==x[1]:
            Total_points=Total_points+1 
    print (Total_points)
football(["3:1", "2:2", "0:1","4:4",'5:2'])    
    
            
    