# PulPy (Pulses in Python) Tutorials
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jonbmartin/pulpy-tutorials/HEAD)

This is a collection of jupyter notebooks demonstration the functionality of the PulPy python package for MR RF pulse and gradient waveform design. These notebooks are Binder-enabled - click on the badge above for an interactive notebook demonstrating the toolbox, or use one of the badges below to jump to a specific demo. 

Description for notebooks: 

## Adibatic pulse design
This notebook demonstrates the analytic design of a few classes of adiabatic RF pulses - a BIR-4 excitation pulse, a hyperbolic secant inversion pulse, and WURST/GOIA-WURST.

## SLR pulse design
This notebook walks through the basics of PulPy SLR design, which is based on John Pauly's MATLAB SLR pulse design toolkit. Advanced methods such as pulse root-flipping and recursive SLR design are demonstrated as well.

## Multiband pulse design
This notebook builds on the SLR pulse design notebook by multibanding a conventional SLR RF pulse for excitation in a simultaneous multislice imaging sequence. PINS multiband pulse design is also demonstrated.

## VERSE for B1+ Selective Pulses
This notebook was inspired by a recent research project! We have experimented with a class of B1+-selective RF pulses as a part of B0-gradient free imaging systems. These systems often use low-cost amplifiers, and the particular class of amplifier we were investigating was only able to produce constant-amplitude waveforms. This notebook designs a B1+-selective pulse by the Bloch-Siegert localized method, then uses VERSE to flatten the amplitude of the pulse.

## Time-Segmented pTx
This notebook demonstrates a basic small tip angle pTx pulse design using a spiral excitation trajectory, and shows how off-resonance may be incorporated into the design. 

## pTx spokes
This notebook demonstrates a simple pTx spokes pulse design. 

## 1D Slice-Selective Optimal Control
This notebook walks through an iterative optimal control pulse design for a large-tip angle RF pulse.

