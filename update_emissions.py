import netCDF4 as nc

def updateNetCDFfile(fname,varname,newvals):
    dset = nc.Dataset(fname,'r+')
    a = dset.variables[varname]
    m=0   
    for t in range(len(a[:,0,:,:])):
        for i in range(len(a[0,0,:,:])):
            for j in range(len(a[0,0,0,:])):                                    
                if a[t][0][i][j] < newvals[t][0][i][j]:
                    dset.variables[varname][t,0,i,j] = newvals[t,0,i,j]
                    m+=1                    
    print(f'updated {m} elements for {varname}')                    
    dset.close()
    return

infile_edgar = r'./EDGAR/wrfchemi_00z_d03.nc'
infile_vein  = r'./VEIN/wrfchemi_00z_d03.nc'

df = nc.Dataset(infile_vein,'r')

k=0
for v in df.variables:
    var = df.variables[f'{v}'] #[0]
    
    if k < 8: #skipping first 7 variables not updatable
        print(f'skipping for {v}')
        print(f'not updatable variable.')
    else:
        print(f'starting chemical variables')
        print(f'trying to update for {v}')
        try:
            updateNetCDFfile(infile_edgar,f'{v}', var)
        except KeyError:
            print(f'There is no {v}')
    k+=1