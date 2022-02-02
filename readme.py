from peeling.fuzzy import samples_to_fuzzy_projection
from peeling.examples import banana_data, banana_model, pickle_dump, pickle_load
from peeling.peeling import data_peeling_algorithm, data_peeling_backward, peeling_to_structure,uniform
from peeling.plots import plot_fuzzy, plot_peeling_nxd, plot_peeling_nxd_back, plot_scattermatrix
from peeling import *

from matplotlib import pyplot
import scipy.stats as stats

if __name__ == '__main__':
    
    # x = pickle_load('banana_1_degenerate_last_level') 

    # plot_scattermatrix(x,figsize=(7,7))

    # a,b = data_peeling_algorithm(x)
    # f,p = peeling_to_structure(a,b)
    # plot_peeling_nxd(x,a,b,p=p,figsize=(10,10))

    # x = banana_data(n=300,d=3)
    # pickle_dump(x)



    # FORWARD PEELING

    # x = pickle_load('banana_3')
    # x = banana_data(n=100,d=2)

    # print(x.shape)

    # a,b = data_peeling_algorithm(x)

    # f,p = peeling_to_structure(a,b,kind='scenario',beta=0.01)

    # plot_peeling_nxd(x,a,b,p=p,figsize=(9,9),grid=False)

    # BACKWARD PEELING

    n=100
    d_=3
    x = stats.norm(loc=0,scale=2).rvs(size=(n,d_))
    f = banana_model
    y = f(x)

    _,d = y.shape
    x_lo, x_hi = d_*[-10], d_*[10]
    ux = uniform(x_lo, x_hi, N=10_000)
    uy = f(ux)


    a,b,c = data_peeling_backward(uy,y,tol=1e-1)
    fy,p = peeling_to_structure(a,b,kind='scenario',beta=0.01)
    fx = samples_to_fuzzy_projection(ux,a,c)

    plot_fuzzy(fx,p=p,grid=True,figsize=(12,7))

    plot_peeling_nxd(y,a,b,p=p,figsize=(9,9),grid=False,label='Y')
    plot_peeling_nxd_back(ux,a,c,p=p,baseline_alpha=0.9)

    pyplot.show()