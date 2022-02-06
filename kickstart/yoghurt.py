class Yoghurt:
    def __init__(self, yog_num, yog_per_day):
        self.yog_num = yog_num
        self.yog_per_day = yog_per_day
        self.buckets = [0] * [yog_num + 1]

    def consume(self):
        for i in range(self.yog_num, 1):
            ai = int(input())
            if ai > self.yog_num:
                ai = self.yog_num
            self.buckets[ai] += 1
