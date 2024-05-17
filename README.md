# Airfoil in kevlar-walled windtunnel
This benchmark case consist of measurements of a NACA63018 airfoil in a Kevlar-walled windtunnel and the associated tasks are described in the paper (State of Open-source Software for Microphone Array Processing).

The document `NACA63018_acoustic.pdf` describes the setup and geometry. The dataset can be downloaded from: [data.dtu.dk](https://doi.org/10.11583/DTU.c.7222614).

# Bechmark case
The tasks are:

1. Given the time-domain data file: `DTU_PLCT_NACA63018_trip_5PS_5SS_U0_50_AoA_0_TimeSeries.h5` and associated sample rate: Compute the Cross-spectral matrix (CSM) using Welch's method [Welch1967] with `n=4096`, 50% overlap, and a Hanning window. Store real and imaginary parts of the CSM for frequency bins 500Hz and 1000Hz in CSV files named  `data/task1_[institution]_[software]_CSM_[real/imag]_f_[500/1000].csv`.  
**Compare deviations in each case.**
2. Given the microphone array geometry found in the time-domain data file: 
`DTU_PLCT_NACA63018_trip_5PS_5SS_U0_50_AoA_0_TimeSeries.h5`. Compute the Point-spread function (PSF) from a reference point `(x_0,y_0) = (0.0,0.0)` in the domain $x=[-1;1]$ m and $y = [-1;1]$ m using 41 points in each dimension for the plane at $z_0 = 2.3$ m. Use the steering vector formulation III as defined in [Sarradj2012] and store the PSF for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/task2_[institution]_[software]_PSF_f_[500/1000/2000/4000].csv`.  
**Compare PSF plots for each frequency**.
3. Given the cross-spectral matrix data file: 
`DTU_PLCT_NACA63018_trip_5PS_5SS_U0_50_AoA_0_octave-12_CsmEss.h5`, associated microphone array geometry, and source distance $z_0 = 2.3$. Apply diagonal removal, and compute the conventional beamforming acoustic image in the domain $x=[-2;2]$ m and $y = [-1;1]$ m (using 81 points in the x-dimension and 41 in the y-dimension) in the frequency range $(fmin,fmax) = (400,4000)$. Use the steering vector formulation III as defined in [Sarradj2012] and store the acoustic images in dB for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/task3_[institution]_[software]_CBF_f_[500/1000/2000/4000].csv`.  
**Compare acoustic maps for each frequency**.
4. Using the above setup, compute acoustic maps with Clean-SC [Sijtsma2007] using a loop-gain of 0.5, and maximum iterations of 100. Use the steering vector formulation III as defined in [Sarradj2012] and store the acoustic images in dB for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/task4_[institution]_[software]_CleanSC_f_[500/1000/2000/4000].csv`.  
**Compare acoustic maps for each frequency**.
5. Compute Task 3 (CBF) again, but with a shear-layer correction, given the position of the Kevlar wall 1.5m from the trailing edge and 0.8m from the microphone array, and the flow-speed given in the dataset. Assume a plane and thin shear-layer if using [Amiet1978]. Store the acoustic images in dB for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/task5_[institution]_[software]_CBF_f_[500/1000/2000/4000].csv`.   
**Compare acoustic maps for each frequency**.
6. Using the acoustic maps from Task 5, compute source integration for the region $(xmin,xmax,ymin,ymax) = (-0.5,0.5,-0.4,0.4)$ in the frequency range $(fmin,fmax) = (400,4000)$. Store the result as two columns, first column `fc` and second column dB in CSV file name:
`data/task6_[institution]_[software]_CBF_srcint.csv`.   
**Compare source integration results**.
7. Compute Task 4 (Clean-SC) again, but with a shear-layer correction, given the position of the Kevlar wall 1.5m from the trailing edge and 0.8m from the microphone array, and the flow-speed given in the dataset. Assume a plane and thin shear-layer if using [Amiet1978]. Store the acoustic images in dB for frequencies 500Hz, 1000Hz, 2000Hz, and 4000Hz in CSV file names:
`data/task7_[institution]_[software]_CleanSC_f_[500/1000/2000/4000].csv`.   
**Compare acoustic maps for each frequency**.
8. Using the acoustic maps from Task 7, compute source integration for the region $(xmin,xmax,ymin,ymax) = (-0.5,0.5,-0.4,0.4)$. Store the result in dB in CSV file names:
`data/task8_[institution]_[software]_CleanSC_srcint.csv`.   
**Compare source integration results**. 

# Adding a benchmark contribution
Any institution/person using open source software can submit a solution to this benchmark. You can create a pull request with (preferably) a jupyter notebook showing your results. Please name the file `[institution]_[software]` The data that you create in each task should also be added to `/data` and will be compared to the other solutions. You should also add information on how to reproduce the environment that you are using, e.g., with a conda environment or a list of dependencies.

# Citation
This benchmark can be cited by 

```   
Lylloff, O., & Herold, G., & Kujawski, A., & Sarradj, E. (2024). State of open source software for microphone array processing. 10 Th Berlin Beamforming Conference 2024 (BeBeC), Berlin, Germany, 10/06/2024.
```
and the data by:
```   
Lylloff, Oliver Ackermann; Bak, Christian; Fischer, Andreas; Olsen, Anders Smærup; Ildvedsen, Sigurd Lundsgaard; Beckerlee, Jimmie Stig; et al. (2024). PLCT-data: NACA63018 aeroacoustic - microphone array. Technical University of Denmark. Collection. https://doi.org/10.11583/DTU.c.7222614
```

# References
[Welch1967]: Welch, P. (1967). The use of fast Fourier transform for the estimation of power spectra: A method based on time averaging over short, modified periodograms. IEEE Transactions on Audio and Electroacoustics, 15(2), 70–73. https://doi.org/10.1109/TAU.1967.1161901

[Amiet1978]: Amiet, R. K. (1978). Refraction of sound by a shear layer. Journal of Sound and Vibration, 58(4), 467–482. https://doi.org/10.1016/0022-460X(78)90353-X

[Sarradj2012]: Sarradj, E. (2012). Three-dimensional acoustic source mapping with different beamforming steering vector formulations. Advances in Acoustics and Vibration, 2012(4), 1–12. https://doi.org/10.1155/2012/292695

[Sijtsma2007]: Sijtsma, P. (2007). CLEAN based on spatial source coherence. International Journal of Aeroacoustics, 6(4), 357–374.