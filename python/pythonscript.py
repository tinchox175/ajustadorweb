import json
import asyncio
from js import document, FileReader, console, JSON, Bokeh
from pyodide import create_proxy
import numpy as np
from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.resources import CDN
from scipy.optimize import curve_fit


document.getElementById("content").innerHTML = ''
p = figure(plot_width=1000, plot_height=600)
p.circle(0, 0)
p_json = json.dumps(json_item(p))
Bokeh.embed.embed_item(JSON.parse(p_json), "plot")

async def process_file(event):
      fileList = event.target.files.to_py()
      for f in fileList:
        data = await f.text()
        lista = data.split("\r\n")
        lista = data.split("\n")
        for i in range(len(lista)):
          lista[i-1].replace(';',',')
          lista[i-1] = lista[i-1].split(',')
        data = np.array(lista)
        global data1
        data1 = []
        global data2
        data2 = []
        i = 0
        while i<(len(data)-1):
            print(data[i][0])
            print(type(data[i][0]))
            if data[i][0]=='' or data[i][1]=='' or any(c.isalpha() for c in data[i][0]) or any(c.isalpha() for c in data[i][1]):
                pass
            else:
                data1.append(data[i][0])
            i+=1
        i = 0
        while i<(len(data)-1):
            if data[i][0]=='' or data[i][1]=='' or any(c.isalpha() for c in data[i][1]) or any(c.isalpha() for c in data[i][0]):
                pass
            else:
                data2.append(data[i][1])
            i+=1
        data1 = np.array(data1, dtype=np.float64)
        print(data1)
        data2 = np.array(data2, dtype=np.float64)
        print(data2)
        global data3
        data3 = [data1,data2]
        document.getElementById("content").innerHTML = ''
        document.getElementById("plot").innerHTML = ''
        document.getElementById("parametros-output").innerHTML = 'Cargado.'
        p = figure(plot_width=1000, plot_height=600)
        p.line(data1, data2, line_width = 1)
        p.circle(data1, data2)
        p_json = json.dumps(json_item(p))
        Bokeh.embed.embed_item(JSON.parse(p_json), "plot")
        #document.getElementById("content").innerHTML = data3


file_event = create_proxy(process_file)
 
e = document.getElementById("myfile")
e.addEventListener("change", file_event, False)

async def guarda(event):
  global funcionajustadora
  funcionajustadora = Element('funcionajusta').element.value

guardar = create_proxy(guarda)

a = document.getElementById("funcionajusta")
a.addEventListener("input", guardar, False)

async def guarda(event):
  global p1
  p1 = Element('par1').element.value
guardar = create_proxy(guarda)
par1 = document.getElementById("par1")
par1.addEventListener("input", guardar, False)

async def guarda(event):
  global p2
  p2 = Element('par2').element.value
guardar = create_proxy(guarda)
par2 = document.getElementById("par2")
par2.addEventListener("input", guardar, False)

async def guarda(event):
  global p3
  p3 = Element('par3').element.value
guardar = create_proxy(guarda)
par3 = document.getElementById("par3")
par3.addEventListener("input", guardar, False)

async def guarda(event):
  global p4
  p4 = Element('par4').element.value
guardar = create_proxy(guarda)
par4 = document.getElementById("par4")
par4.addEventListener("input", guardar, False)

async def guarda(event):
  global p5
  p5 = Element('par5').element.value
guardar = create_proxy(guarda)
par5 = document.getElementById("par5")
par5.addEventListener("input", guardar, False)

def ajuste(x,a,b,c,d,e):
  try:
    y = eval(funcionajustadora)
    print(type(y))
  except SyntaxError:
    y = 0
  return y

def exceptor():
  try:
      p = figure(plot_width=1000, plot_height=600)
      p.circle(data1, data2)
      p.line(data1, data2, line_width = 1)
      p_json = json.dumps(json_item(p))
      Bokeh.embed.embed_item(JSON.parse(p_json), "plot")
      document.getElementById("parametros-output").innerHTML = 'Tu función es inválida.'
  except:
      p = figure(plot_width=1000, plot_height=600)
      p.circle(0, 0)
      p_json = json.dumps(json_item(p))
      Bokeh.embed.embed_item(JSON.parse(p_json), "plot")
      document.getElementById("parametros-output").innerHTML = 'Tu archivo es inválido.'

async def nib(event):
  global popt
  pcero = [1,1,1,1,1]
  try:
    pcero[0]= float(p1)
  except NameError:
    pass
  except ValueError:
    pass
  try:
    pcero[1]= float(p2)
  except NameError:
    pass
  except ValueError:
    pass
  try:
    pcero[2]= float(p3)
  except NameError:
    pass
  except ValueError:
    pass
  try:
    pcero[3]=float(p4)
  except NameError:
    pass
  except ValueError:
    pass
  try:
    pcero[4]= float(p5)
  except NameError:
    pass
  except ValueError:
    pass
  try:
    popt, pcov = curve_fit(ajuste, data1[:len(data2)], data2, p0=pcero)
  except ValueError:
    try:
      popt, pcov = curve_fit(ajuste, data1, data2[:len(data1)], p0=pcero)
    except ValueError:
      exceptor()
  except RuntimeError:
    pass
  except:
    exceptor()
    return
  p = figure(plot_width=1000, plot_height=600)    
  try:
    p.line(data1, ajuste(data1, *popt), line_width=2, line_color="orange")
  except NameError:
    p.line(data1, data2, line_width = 1)
    p.circle(data1, data2)
    p_json = json.dumps(json_item(p))
    Bokeh.embed.embed_item(JSON.parse(p_json), "plot")
    document.getElementById("parametros-output").innerHTML = 'No se pudo ajustar tus datos, proba mejorando la función o los parámetros de búsqueda.'
    return
  global Sumsquare
  try:
    Sumsquare = np.sum((data2-ajuste(data1, *popt))**2)
    TSS = np.sum((data2-np.full(len(data2),np.mean(data2)))**2)
    SEE = np.sqrt(np.sum((data2-ajuste(data1,*popt))**2)/len(data2))
  except NameError:
    pass
  p.line(data1, data2, line_width = 1)
  p.circle(data1, data2)
  p_json = json.dumps(json_item(p))
  Bokeh.embed.embed_item(JSON.parse(p_json), "plot")
  document.getElementById("parametros-output").innerHTML = f'Los parametros son: a = {popt[0]}, b = {popt[1]}, c = {popt[2]}, d = {popt[3]}, e = {popt[4]} .\n RSS vale aproximadamente {np.round(Sumsquare,3)}. R² vale aproximadamente {np.round(1-Sumsquare/TSS,3)}. S vale aproximadamente {np.round(SEE,3)}'
  

you = create_proxy(nib)

b = document.getElementById("yo")
b.addEventListener("click", you, False)

async def limpiadora(event):
  p.circle(0, 0)
  p_json = json.dumps(json_item(p))
  Bokeh.embed.embed_item(JSON.parse(p_json), "plot")

limpia = create_proxy(limpiadora)

clear = document.getElementById("btn")
clear.addEventListener("click", limpia, False)
