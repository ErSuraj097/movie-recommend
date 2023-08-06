import zipfile
import pickle


from zipfile import ZipFile

# # specifying the zip file name
# file_name = "./similarity.zip"

# # opening the zip file in READ mode
# with ZipFile(file_name, 'r') as zip:
# # printing all the contents of the zip file
#     zip.printdir()
   
# #
# # cPickle.loads works
# data = zip.read('similarity.zip')
# zf = zipfile.ZipFile('similarity.zip', 'r')

# sd1 = pickle.load(zf.open('similarity.pkl'))


# #
# # cPickle.load doesn't work
# #
# zf = zipfile.ZipFile('zipped_pickle.zip', 'r')
# sd2 = cPickle.load(zf.open('data.pkl'))
# zf.close()

# import bz2
# import pickle
# import pickle as cPickle
# import bz2file as bz2
# # Saves the "data" with the "title" and adds the .pickle
# def compressed_pickle(title, data):

#     with bz2.BZ2File(title + ‘.pbz2’, ‘w’) as f:
#         pickle.dump(data, f)
        
# data  = ./similarity
# compressed_pickle("similarity2",data)

# import bz2
# data = "similarity.pkl"
# c = bz2.compress(data)
# d = bz2.decompress(c)
# print(d)
import gzip
similarity = pickle.load(open('similarity.pkl','rb'))
with gzip.open(similarity, 'rb') as f:
    file_content = f.read()