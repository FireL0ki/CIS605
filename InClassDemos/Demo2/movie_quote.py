# project: In class demo - demo 2
# description: demonstrate loops

class Movie_Quote:
    def __init__(self, quote): 
        self.quote = quote

    def for_loop_example1(self):

        result = ""

        # range starts at 0, includes first number, goes up to final number, not including final number in this example [0,1,2,3,4,5,6,7,9]
        # can take 3 arguments [start, step, end]
        # default start = 0 / default step = 1 / end is required
        for r in range(10):
            # \t is for tab as \n is for new line
            result += f"{r}\t{self.quote}\n"

        print(result)

    def for_loop_example2(self):

        result = ""

        for r in range(10, 21):
            result += f"{r}\t{self.quote}\n"
        
        print(result)

    def while_loop_example1(self):

        n = 1
        LIMIT = 10
        result = ""

        while n <= LIMIT:
            result += f"{n}\t{self.quote}\n"
            # increment n - ensure the condition will become false to end loop
            n += 1

        print(result)


    # do while loop example -- have the loop run at least once
    def while_loop_example2(self):

        n = 1
        LIMIT = 10
        result = ""

        # true will always be true, so it will enter the body of the loop
        while True:
            result += f"{n}\t{self.quote}\n"
            
            # end loop
            if n > 0:
                break

        print(result)