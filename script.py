import matplotlib.pyplot as plt
import numpy as np
import os


class GraphVars():
    def __init__(self):
        # str
        self._title = None
        self._xlabel = None
        self._ylabel = None
        self._plot_name = None
        self._data_label = None
        self._label = None
        # list
        self._plot_names = None
        self._data_label = None
        self._labels = None

def main():
    def read_data():

        '''
        Lê o arquivo de dados
        '''

        data = open('plots.slevel.txt', 'r')
        return data


    def start_name(GraphVars):
        
        '''
        Pega os nomes dos plots disponíveis
        '''

        GraphVars._plot_names = list()
        for line in data:
            if line.startswith('start_plot'):
                GraphVars._plot_name = line.split()[1]
                GraphVars._plot_names.append(GraphVars._plot_name)
        return GraphVars._plot_names


    def get_labels(GraphVars):

        '''título do gráfico''' 

        data = read_data()
        GraphVars._data_labels = list()
        GraphVars._labels = list()
        text = []
        record = False
        for line in data:
            if line.startswith('start_plot ' + GraphVars._plot_name): 
                record = True
                text = []
            if record:
                text.append(line)
            if line.startswith('end_plot'):
                record = False
                
                with open("%s-data.dat" % GraphVars._plot_name,"w") as new_file:
                    lines =''.join(text)  # limpa o cabeçalho das linhas
                    new_file.write(lines)
                new_file.close()

        with open("%s-data.dat" % GraphVars._plot_name,"r") as read_file:
            for line in read_file:
                if line.startswith('   title ='): 
                    GraphVars._title = line.strip('title =').replace("'","")
                if line.startswith('   xlabel='): 
                    GraphVars._xlabel = line.split('xlabel=')[1].replace("'","")
                if line.startswith('   ylabel='): 
                    GraphVars._ylabel = line.split('ylabel=')[1].replace("'","")
                if line.startswith('   data'):
                    GraphVars._data_label = line.strip()
                    GraphVars._label = ''.join(GraphVars._data_label).split()[3].replace("'","")
                    GraphVars._data_labels.append(GraphVars._data_label)
                    GraphVars._labels.append(GraphVars._label)
                if line.startswith('end_plot'): 
                    line = line.strip()
                    GraphVars._data_labels.append(line)
        return 




    def get_data(GraphVars):

        '''
        Extrai os dados para o plot
        '''


        init_targets = GraphVars._data_labels[:-1]
        end_targets = GraphVars._data_labels[1:]
        labels = GraphVars._labels
        record = False
        text = []

        

        for i in range(0,len(labels)):
            with open("%s-data.dat" % GraphVars._plot_name,"r") as read_file:
                for line in read_file:
                    if line.startswith('start_plot ' + GraphVars._plot_name): continue
                    if line.startswith('   ' + init_targets[i]): 
                        record = True
                        text =[]
                    if record:
                        text.append(line.strip())
                    if line.startswith('   ' + end_targets[i]):
                        record = False
                    if line.startswith('end_plot'):
                        record = False

                        with open("%s-data.dat" % labels[i],"w") as new_file:
                            lines ='\n'.join(text[1:-1])  # limpa o cabeçalho das linhas
                            new_file.write(lines)
                        new_file.close()
        return 
            
    def plot_data(GraphVars):

        '''
        Plota o gráfico
        '''

        labels = GraphVars._labels
        colors = ['#ff0000','#993399','#003300','#66ccff','#ffff00','#996600','#ff9900',
                '#6666ff','#006699','#000066','#000000','#99ff99','#669999','#ccff33',
                '#663300','#ffbf80', '#ff6600','#ff66ff','#cc3399','#3366cc']
        axis = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                'q','i','j','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
        # fig, ax = plt.subplots(figsize=(6.5,6.0))
        fig, ax = plt.subplots()

        for i in range(0,len(labels)):

            # open data for plot

            axis[i], y = np.loadtxt('%s-data.dat' % labels[i], unpack = True)

            # ploting data

            ax.plot(axis[i],y,color=colors[i])
            ax.legend(labels,loc='best')
            


        # axis

        ax.set_xlabel(GraphVars._xlabel)
        ax.set_ylabel(GraphVars._ylabel)
        ax.set_title(GraphVars._title)
        
        
        ax.secondary_xaxis('top').set_xticklabels([])
        ax.secondary_yaxis('right').set_yticklabels([])

        plt.ticklabel_format(axis='y',style='sci', scilimits=(0,0))

        


        plt.savefig('%s.pdf' % GraphVars._plot_name)
        

        # removing created files

        os.system('rm *.dat')

        return

    data = read_data()

    def start(GraphVars):
        
        nfp = start_name(GraphVars)
        i = 0
        print("")
        print("")
        print("")
        print("These are the available plots in the data file:")
        print("")
        print("")
        print("")
        print("Please, choose the kmc plot by name")
        print("")
        print("")
        print("")
        for name in nfp:
            print('('+ str(i) + ')', name)
            i += 1 
        print("")
        print("")
        print("")
        return nfp


    nfp = start(GraphVars)
    name_plot = input("What plot do you choose? ")
    while name_plot != 'exit':
        
        if name_plot not in nfp:
            print("")
            print("")
            print("")
            print("ERROR: Wrong name")
        else:
            GraphVars._plot_name = name_plot

        get_labels(GraphVars)
        get_data(GraphVars)
        plot_data(GraphVars)
        name_plot = input("What plot do you choose? ")
    if name_plot == 'exit':
        answer = input('Do you want to join all graphics?(y/n) ')
        if answer == 'y':
            fnfp = input('Insert name for plot: ')
            os.system('pdftk *.pdf output %s.pdf' % fnfp)
            print('Done!')
        else:
            print('Done!')

    
        
        


    


main()