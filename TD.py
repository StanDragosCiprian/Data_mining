class TopicsDictionary:
    def __init__(self,topic,vector) :
        self.topic=topic
        self.vector=vector
    def get_topic(self):
        return self.topic
    
    def get_vector(self):
        return [int(i[0]) for i in self.vector]