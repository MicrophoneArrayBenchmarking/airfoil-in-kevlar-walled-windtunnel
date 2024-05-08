# Airfoil in kevlar-walled windtunnel
This benchmark case consist of measurements of a NACA63018 airfoil in a Kevlar-walled windtunnel and the associated tasks are described in the paper (State of Open-source Software for Microphone Array Processing).

The document `NACA63018_acoustic.pdf` describes the setup and geometry. The dataset can be downloaded from: [data.dtu.dk](https://data.dtu.dk) (awaiting data review and official DOI).

# Bechmark case
The tasks are:

1. Given the time-domain data file: `DTU_PLCT_NACA63018_trip_5PS_5SS_U0_50_AoA_0_TimeSeries.h5` and associated sample rate: Compute the Cross-spectral matrix (CSM) using Welch's method with `n=4096`, 50% overlap, and a Hanning window. Store real and imaginary parts of the CSM for frequency bins 500Hz and 1000Hz in CSV files named  `data/[institution]_[software]_task1_CSM_[real/imag]_f_[500/1000].csv`.  
**Compare deviations in each case.**
2. Given the microphone array geometry found in the time-domain data file: 
`DTU_PLCT_NACA63018_trip_5PS_5SS_U0_50_AoA_0_TimeSeries.h5`. Compute the Point-spread function (PSF) from a reference point `(x_0,y_0) = (0.0,0.0)` in the domain $x=[-1;1]$ m and $y = [-1;1]$ m using 41 points in each dimension for the plane at $z_0 = 2.3$ m. Use the steering vector formulation III as defined in [Sarradj2012] and store the PSF in dB for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/[institution]_[software]_task2_PSF_f_[500/1000/2000/4000].csv`.  
**Compare PSF plots for each frequency**.
3. Given the cross-spectral matrix data file: 
`DTU_PLCT_NACA63018_trip_5PS_5SS_U0_50_AoA_0_octave-12_CsmEss.h5`, associated microphone array geometry, and source distance $z_0 = 2.3$. Apply diagonal removal, and compute the conventional beamforming acoustic image in the domain $x=[-2;2]$ m and $y = [-1;1]$ m using 41 points in each dimension in the frequency range $(fmin,fmax) = (400,4000)$. Store the acoustic images in dB for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/[institution]_[software]_task3_CBF_f_[500/1000/2000/4000].csv`.  
**Compare acoustic maps for each frequency**.
4. Find source location (max peak?) and compare. Compute source integration over the region $(xmin,xmax,ymin,ymax) = (...)$ and plot the results in dB as function of frequency. Compare and show deviation.
5. Same as above, but with shear-layer correction, given position of Kevlar wall.
6. Using above setup, use Clean-SC/DAMAS in frequency range `(fmin,fmax) = (400,4000)` and compute acoustic maps and compare. Plot source integration in region $(xmin,xmax,ymin,ymax) = (...)$ and plot as function of frequency.  
**Show deviation.**

# Adding a benchmark contribution
Any institution/person using open source software can submit a solution to this benchmark. You can create a pull request with (preferably) a jupyter notebook showing your results. Please name the file `[institution]_[software]` The data that you create in each task should also be added to `/data` and will be compared to the other solutions. You should also add information on how to reproduce the environment that you are using, e.g., with a conda environment or a list of dependencies.

# References
[Sarradj2012]: Sarradj, E. (2012). Three-dimensional acoustic source mapping with different beamforming steering vector formulations. Advances in Acoustics and Vibration, 2012(4), 1–12. https://doi.org/10.1155/2012/292695