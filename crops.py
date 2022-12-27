from flask import Flask,request
from flask_restful import Resource,Api
import json


app = Flask(__name__)
api = Api(app)


response = []

class home(Resource):
    def get(self):
        return {"message" : "Hey, welcome to dummy cropdata api"}

class getAllCrops(Resource):
    def get(self):
        f = open('data (1).json')
        cropData = json.load(f)

        #cropname, pageno, 
        crop=request.args.get('crop', type=str)
        pageno=request.args.get('pageno', type=int)
        limit=request.args.get('limit', type=int)

        if limit == None:
            limit=10
        
        if crop == None:
            if pageno == None:
                return cropData['all']
            elif pageno==0:
                offset=0
            else:
                offset=(limit)*pageno
        elif crop!= None and pageno == None:
            offset=0
        elif crop!= None and pageno !=None:
            if pageno==0:
                offset=0
            else:
                offset=(limit)*pageno


        # if pageno == None:
        #     return cropData['all']
        # elif pageno==0:
        #     offset=0
        # else:
        #     offset=(limit)*pageno


        

        
        # limit=offset
       

        new_list=cropData['all']
        if crop == None:
            return new_list[offset:(offset+10)],200
        else:
            empty_list=list(filter(lambda x:x['Crop'] == crop , new_list))

        
        

        try:
            response = empty_list
            return response[offset:(offset+10)],200
        except Exception as e:
            return e.message, 500

    
        
        # print(cropData)




        

api.add_resource(home,'/',endpoint = '')
api.add_resource(getAllCrops,'/all',endpoint = 'all' )

if __name__ == '__main__':
    app.run()


