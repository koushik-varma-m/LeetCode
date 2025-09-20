class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_food_rating=defaultdict(list)
        self.food_rating=defaultdict(int)
        self.food_cuisine=defaultdict(str)
        for i in range(len(foods)):
            self.food_rating[foods[i]]=-1*ratings[i]
            self.food_cuisine[foods[i]]=cuisines[i]
            heapq.heappush(self.cuisine_food_rating[cuisines[i]],(-1*ratings[i],foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine=self.food_cuisine[food]
        self.food_rating[food]=-1*newRating
        heapq.heappush(self.cuisine_food_rating[cuisine],(-1*newRating,food))
    def highestRated(self, cuisine: str) -> str:
        heap=self.cuisine_food_rating[cuisine]
        while heap:
            cur_r, cur_f=heap[0]
            if self.food_rating[cur_f]!=cur_r:
                heapq.heappop(heap)
            else:
                break
        self.cuisine_food_rating[cuisine]=heap
        return heap[0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)