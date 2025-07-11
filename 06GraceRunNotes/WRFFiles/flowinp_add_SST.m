% This script adds SST data to the WRF input files.
% It's the original script provided by Dan Fu.

clear;clc;close all



infile='wrflowinp_d01_backup';

file='wrflowinp_d01';

system(['cp ',infile,' ',file]);

%system(['nccopy -d 5 ',infile,' ',file]);

%ncid = netcdf.write('myfile.nc','CLOBBER');

ncid = netcdf.open(file,'NC_WRITE');

varid = netcdf.getConstant('GLOBAL');

netcdf.putAtt(ncid,varid,'START_DATE','2023-01-01_00:00:00');

netcdf.close(ncid);



XLONG=ncread('wrfinput_d01','XLONG');

XLAT=ncread('wrfinput_d01','XLAT');



SSTold=ncread(file,'SST');

[xlen,ylen,tlen]=size(SSTold);

SSTold=reshape(SSTold,[xlen,ylen,8,tlen/8]);



[Yhr,Xhr]=meshgrid(-89.99:0.01:89.99,-179.99:0.01:180);

OBS=dir(['*GHRSST*.nc']);

for i=1:tlen/8;

    i

    obsfile=OBS(i).name;

    SSTobs=ncread(obsfile,'analysed_sst');

    F=griddedInterpolant(Xhr,Yhr,SSTobs);

    dummy=F(XLONG,XLAT);dummy(isnan(dummy))=0;

    for t=1:8;

        SST(:,:,t,i)=dummy;

    end

end

SST=reshape(SST,[xlen,ylen,tlen]);

ncid=netcdf.open(file,'NC_WRITE');

SSTid=netcdf.inqVarID(ncid,'SST');

netcdf.putVar(ncid,SSTid,SST);

netcdf.close(ncid); 



SST=SST(:,:,1);

file='wrfinput_d01';

ncid=netcdf.open(file,'NC_WRITE');

SSTid=netcdf.inqVarID(ncid,'SST');

netcdf.putVar(ncid,SSTid,SST);

netcdf.close(ncid); 







%%%%%%%%%%%%%%

%%%%%%%%%%%%%%

%%%%%%%%%%%%%%

clear SST

infile='wrflowinp_d02_backup';

file='wrflowinp_d02';

system(['cp ',infile,' ',file]);

%system(['nccopy -d 5 ',infile,' ',file]);

%ncid = netcdf.write('myfile.nc','CLOBBER');

ncid = netcdf.open(file,'NC_WRITE');

varid = netcdf.getConstant('GLOBAL');

netcdf.putAtt(ncid,varid,'START_DATE','2023-01-01_00:00:00');

netcdf.close(ncid);



XLONG=ncread('wrfinput_d02','XLONG');

XLAT=ncread('wrfinput_d02','XLAT');



SSTold=ncread(file,'SST');

[xlen,ylen,tlen]=size(SSTold);

SSTold=reshape(SSTold,[xlen,ylen,8,tlen/8]);



[Yhr,Xhr]=meshgrid(-89.99:0.01:89.99,-179.99:0.01:180);

OBS=dir(['*GHRSST*.nc']);

for i=1:tlen/8;

    i

    obsfile=OBS(i).name;

    SSTobs=ncread(obsfile,'analysed_sst');

    F=griddedInterpolant(Xhr,Yhr,SSTobs);

    dummy=F(XLONG,XLAT);dummy(isnan(dummy))=0;

    for t=1:8;

        SST(:,:,t,i)=dummy;

    end

end

SST=reshape(SST,[xlen,ylen,tlen]);

ncid=netcdf.open(file,'NC_WRITE');

SSTid=netcdf.inqVarID(ncid,'SST');

netcdf.putVar(ncid,SSTid,SST);

netcdf.close(ncid);   



SST=SST(:,:,1);

file='wrfinput_d02';

ncid=netcdf.open(file,'NC_WRITE');

SSTid=netcdf.inqVarID(ncid,'SST');

netcdf.putVar(ncid,SSTid,SST);

netcdf.close(ncid); 