class Character():
    
    def __init__(self,name):
        self.name=name
        self.inventory=[]
        self.health=10
        self.add_to_db()
        
        @property
        def name(self):
            return self._name
        @name.setter(self,name)
        def name(self,name):
            if isinstance(name,str) and len(name) is range(3,16):
                self._name = name
            else: 
                raise AttributeError("Name must be between 3-15 characters long")
            
        