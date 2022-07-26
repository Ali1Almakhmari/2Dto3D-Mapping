clear;
clc;
%% 2D to 3D Mars Image converter
% Author: Ali Almakhmari
% 2022/06/01

pictureName = "mars.png"; %the 2D picture's name of Mars: "mars.png"

R = 3397200; %Mars equatorial radius in meters
f = 1999/339619; %flatenning factor of Mars

a = R; %semi-major axis in meters
b = (1-f)*a; %semi-minor axis in meters
    
[X,Y,Z] = ellipsoid(0, 0, 0, a, a, b, 800); %coordinates of the ellipsoid that is Mars using 800 panels

pictureData = imread(pictureName); %reading the 2D picture data of Mars
planet = surface(X, Y, Z, "FaceColor", "texture", "EdgeColor", "none", "CData", flipud(pictureData), "DiffuseStrength", 1, "SpecularStrength", 0,"FaceAlpha", 1); %defining surface coordinates needed to draw Mars

%viewing
axis equal;
title("Mars 3D Globe")
xlabel("X (meters)")
ylabel("Y (meters)")
zlabel("Z (meters)")
grid on
view(3);
