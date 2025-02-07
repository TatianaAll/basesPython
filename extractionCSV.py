import csv

def extract(filename, delimiterChosen):
    data = []
    with open(filename, mode = "r") as file_csv:
        csv_reader = csv.DictReader(file_csv, delimiter = delimiterChosen)
        for line in csv_reader : 
            data.append(line)
    return data

def transformHoursInSalary(dataToTransform):
    #une liste vide qui contienddra mon dict pour chaque worker
    newData = []
    for data in dataToTransform:
        #mon nv dict
        transformedData = {}
        #le nom est conservé
        transformedData['nom'] = data["nom"]
        #je transforme les heures travaillées au salaire correspondant
        transformedData["salaire"] = int(data["heures_travaillees"]) * 15
        #j'ajoute la ligne de dict à ma liste vide
        newData.append(transformedData)
    return newData

def loadNewData(dataToLoad, filename, fieldnameChosen):
    with open(filename, mode = "w") as file_csv:
        csv_writer = csv.DictWriter(file_csv, fieldnames = fieldnameChosen)
        csv_writer.writeheader()
        for data in dataToLoad:
            csv_writer.writerow(data)

#les heures travaillées
dataInput = extract("input.csv", ";")
dataInputTransformed = transformHoursInSalary(dataInput)
#print(data_input)
#print(data_input_transformed)
loadNewData(dataInputTransformed, "output.csv", ['nom', 'salaire'])
