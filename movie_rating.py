class movie:
    def __init__(self,title,rating=""):
        self.title=title
        self.rating=rating
    
    def display(self):
        print(f"the movie name is {self.title}")
    
    def rate(self):
        print(f"the rating of {self.title} movie has {self.rating} rating ")
        if len(self.rating)==0:
            print("give some rating ")
        elif len(self.rating)==1 :
            print("good movie")
        elif len(self.rating)==2 :
            print("good movie")
        elif len(self.rating)==3 :
            print("better movie")
        elif len(self.rating)==4 :
            print("better movie")
        elif len(self.rating)==5:
            print("most liked movie by others")
        else:
            breakpoint
kannada=movie("bajarangi")
kannada.rate()
