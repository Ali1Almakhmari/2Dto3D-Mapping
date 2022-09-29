clear
clc
picturePath = "C:\Users\Ali\Desktop\truemap_interploated.tiff"; %the 2D picture's name of Mars: "light.png"

R = 3397200; %Mars equatorial radius in meters
f = 1999/339619; %flatenning factor of Mars

a = R; %semi-major axis in meters
b = (1-f)*a; %semi-minor axis in meters
    
[X,Y,Z] = ellipsoid(0, 0, 0, a, a, b, 1000); %coordinates of the ellipsoid that is Mars using 800 panels

pictureData = imread(picturePath); %reading the 2D picture data of Mars


figure(1);
planet = surface(X, Y, Z, "FaceColor", "texture", "EdgeColor", "none", "CData", flipud(pictureData), "DiffuseStrength", 1, "SpecularStrength", 0,"FaceAlpha", 1); %defining surface coordinates needed to draw Mars

%viewing
axis equal;
grid on
view(0,10);
filename = 'GIF.gif'; %what name to use when saving your GIF
axis off;
set(gcf, 'InvertHardCopy', 'off'); 
set(gcf,'Color',[0 0 0]); % RGB values [0 0 0] indicates black color
for i = 1:360
    rotate(planet,[0 0 1],1)
    frame = getframe(1);
    im = frame2im(frame);
    [imind,cm] = rgb2ind(im,256);
    if i == 1
        imwrite(imind,cm,filename,'gif', 'Loopcount',inf);
    else
        imwrite(imind,cm,filename,'gif','WriteMode','append');
    end
end



