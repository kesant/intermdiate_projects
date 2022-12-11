import pandas 
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_color=data["Primary Fur Color"].unique()
data_color1=data["Primary Fur Color"][data["Primary Fur Color"]==data_color[1]].count()
data_color2=data["Primary Fur Color"][data["Primary Fur Color"]==data_color[2]].count()
data_color3=data["Primary Fur Color"][data["Primary Fur Color"]==data_color[3]].count()
data_dict={
    "colores":[data_color[1],data_color[2],data_color[3]],
    "cantidad":[data_color1,data_color2,data_color3]

}
new_data=pandas.DataFrame(data_dict)
new_data.to_csv("cantidad_colores.csv")