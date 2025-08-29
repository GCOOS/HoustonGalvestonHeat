#!/usr/bin/env python3
"""
This script adds SST data to the WRF input files.
It's from Dan Fu's script, converted to Python.
"""

import os
import shutil
import numpy as np
import netCDF4 as nc
from scipy.interpolate import RegularGridInterpolator
import glob

def process_domain(infile, outfile, wrfinput_file, wrfinput_outfile, has_perturbation=False):
    """Process SST data for a single domain"""
    
    # Copy backup file to working file
    shutil.copy(infile, outfile)
    shutil.copy(wrfinput_file, wrfinput_outfile)

    # Read coordinate grids from wrfinput file
    with nc.Dataset(wrfinput_file, 'r') as wrfinput:
        XLAT = wrfinput.variables['XLAT'][:][0]
        XLONG = wrfinput.variables['XLONG'][:][0]
    
    # Read existing SST data
    with nc.Dataset(outfile, 'r') as ncid:
        SSTold = ncid.variables['SST'][:]
    
    # Get dimensions
    tlen, xlen, ylen = SSTold.shape
    print('tlen, xlen, ylen,', tlen, xlen, ylen)
    
    # Find GHRSST observation files
    OBS_files = glob.glob('*GHRSST*.nc')
    OBS_files.sort()
    
    loop_num = (tlen - 1) // 8 + 1
    print('loop_num', loop_num)
    
    perturbation = np.random.uniform(-0.25, 0.25, size=(xlen, ylen))

    for i in range(loop_num):
        obsfile = OBS_files[i]

        print(f"Processing day {i}, file: {obsfile}")
        
        # Read observed SST data
        with nc.Dataset(obsfile, 'r') as obs_nc:
            obs_SST = obs_nc.variables['analysed_sst'][:]
            obs_lat = obs_nc.variables['lat'][:]
            obs_lon = obs_nc.variables['lon'][:]

        if obs_SST.ndim == 3:
            obs_SST = obs_SST[0, :, :]  # Take first time step if 3D
        
        # Handle masked array - convert to regular array with NaN for masked values
        if np.ma.is_masked(obs_SST):
            obs_SST = np.ma.filled(obs_SST, np.nan)
        
        # Create interpolation function
        F = RegularGridInterpolator(
            (obs_lat, obs_lon), obs_SST, 
            bounds_error=False, fill_value=0
        )
        
        # Interpolate to WRF grid
        points = np.stack([XLAT.ravel(), XLONG.ravel()], axis=-1)
        dummy = F(points).reshape(XLAT.shape)
        
        # Replace NaN values with 0
        dummy[np.isnan(dummy)] = 0
        dummy[SSTold[i*8] == 0] = 0
        
        # Replicate across all 8 time steps for this day
        for t in range(i*8, (i+1)*8):
            if t >= tlen:
                break
            print('Current t', t)
            assert t//8 == i
            if has_perturbation:
                SSTold[t, :, :] = dummy + perturbation
            else:
                SSTold[t, :, :] = dummy
    
    print('Saving the result')
    with nc.Dataset(outfile, 'r+') as ncid1:
        ncid1.variables['SST'][:] = SSTold
    
    SST_first = SSTold[0:1, :, :]
    
    with nc.Dataset(wrfinput_outfile, 'r+') as ncid2:
        # print(ncid2.variables['SST'][:].shape)
        ncid2.variables['SST'][:] = SST_first
        if has_perturbation:
            ncid2.variables['T'][:] = ncid2.variables['T'][:] + perturbation[np.newaxis, np.newaxis, :, :]
            ncid2.variables['T2'][:] = ncid2.variables['T2'][:] + perturbation[np.newaxis, :, :]
        # print(ncid2.variables['SST'][:].shape)

    print('Done')


def main():
    # Change to script directory to handle debug mode
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Process domain 1 (d01)
    process_domain('wrflowinp_d01_backup', 'wrflowinp_d01', 'wrfinput_d01_backup', 'wrfinput_d01', True)
    
    # Process domain 2 (d02)
    process_domain('wrflowinp_d02_backup', 'wrflowinp_d02', 'wrfinput_d02_backup', 'wrfinput_d02', True)


if __name__ == "__main__":
    main()
