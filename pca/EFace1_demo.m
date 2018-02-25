
%UNDERSTANDING PRINCIPAL COMPONENT ANALYSIS On face images

%Here K=Total number of pixels of image=MN=112x92

%RMSE averaged over all images..........Change value of q for PCA
%components

%When q=6(All principal components retained)     err =  00
%When q=5( 5 principal components retained)     err =  9.3270
%When q=4( 4 principal components retained)     err =  21.6476
%When q=3( 3 principal components retained)     err =    29.9518
%--------------------------------------------------------------------------

clc;
clear all;
close all;

%Reading and displaying 6 face images

F1=imread('f1.pgm');
F2=imread('f2.pgm');
F3=imread('f3.pgm');
F4=imread('f4.pgm');
F5=imread('f5.pgm');
F6=imread('f6.pgm');

figure;imshow(F1);title('First image');
figure;imshow(F2);title('Second image');
figure;imshow(F3);title('Third  image');
figure;imshow(F4);title('Forth  image');
figure;imshow(F5);title('Fifth image');
figure;imshow(F6);title('Sixth  image');

S=cat(3,F1,F2,F3,F4,F5,F6);    %Representing images in 3 dimension stack
[X,R]=imstack2vectors(S);       %Convert images from matrix (MxN) to corresponding column vector [ColF1;ColF2;ColF3;ColF4;ColF5;ColF6]

%Covariance matrix Generation  (6x6)

[K,n]=size(X);          
X=double(X);

if n==1
    C=0;
    m=X;
else
    m=sum(X,1)/K;           
    X1=X-m(ones(K,1),:);    
    C=(X1'*X1)/(K-1);       %Covariance  matrix C . size=6x6
    m=m';                   
end


% PRINCIPAL COMPONENT IMPLEMENTATION

m=m';                    
[V,D]=eig(C);            %V =EIGEN VECTORED column matrix; D=Eigen valued diagonal matrix

d=diag(D);               %Extract diagonal elements of D

[d,idx]=sort(d);
d=flipud(d);
idx=flipud(idx);

D=diag(d);
V=V(:,idx);


q=input('Enter the number of principal eigenvectors (<= 6): ');                                       %Use only first q principle components

A=V(:,1:q)';             %q x n principal components x'formation matrix;rows are eigen vectors of C corresponding to the
                                %first q largest eigenvalues.
                                
Mx=repmat(m,K,1);    % Kx6 mean matrix 

X=X-Mx;                     %Mean subtracted images

Y=A*(X') ;                  %size of Y=(qx6)*(6xK)=qxK

X2=(A'*Y)';             %size of X2=((6x3)*(3xK))'=(6xK)'=Kx6

X2=X2+Mx;           % Mean added to reconstruct the images

Y=Y';                   %Kxq  matrix


% m=m';                    %nx1 vector

d=diag(D);
ems=sum(d(q+1:end));

%Covariance matrix of transformed images
    m2=sum(Y,1)/K;           
    Y1=Y-m2(ones(K,1),:);    
    CY=(Y1'*Y1)/(K-1);       %Covariance  matrix C . size=6x6
    

%%Cy=A*C*A';

% Displaying principal component images
    
% g1=Y(:,1);
% g1=reshape(g1,112,92);
% figure;imshow(g1,[]);
% title('First principle component image');
% 
% g2=Y(:,2);
% g2=reshape(g2,112,92);
% figure;imshow(g2,[]);
% title('Second principle component image');
% 
% g3=Y(:,3);
% g3=reshape(g3,112,92);
% figure;imshow(g3,[]);
% title('Third principle component image');
% 
% g4=Y(:,4);
% g4=reshape(g4,112,92);
% figure;imshow(g4,[]);
% title('Fourth principle component image');
% 
% g5=Y(:,5);
% g5=reshape(g5,112,92);
% figure;imshow(g5,[]);
% title('Fifth principle component image');
% 
% g6=Y(:,6);
% g6=reshape(g6,112,92);
% figure;imshow(g6,[]);
% title('Sixth principle component image');
% %--------------------------------------------------------------------------
% Reconstructing images
%--------------------------------------------------------------------------
h1=X2(:,1);
h1=reshape(h1,112,92);
figure;imshow(h1,[]);
title('Reconstructed image1');

 h2=X2(:,2);
 h2=reshape(h2,112,92);
 figure;imshow(h2,[]);
 title('Reconstructed image2');
 
h3=X2(:,3);
h3=reshape(h3,112,92);
figure;imshow(h3,[]);
title('Reconstructed image3');

h4=X2(:,4);
h4=reshape(h4,112,92);
figure;imshow(h4,[]);
title('Reconstructed image4');

h5=X2(:,5);
h5=reshape(h5,112,92);
figure;imshow(h5,[]);
title('Reconstructed image5');

h6=X2(:,6);
h6=reshape(h6,112,92);
figure;imshow(h6,[]);
title('Reconstructed image6');

%Finding Reconstruction error (rmse)



disp('RMSE Errors in reconstruction:');
 D1=double(F1(:,:))-double(h1);
 err1=sqrt(sum(sum(D1.^2))/(K))
 
 D2=double(F2)-double(h2);
err2=sqrt(sum(sum(D2.^2))/(K))
 
 D3=double(F3)-double(h3);
 err3=sqrt(sum(sum(D3.^2))/(K))
 
 D4=double(F4)-double(h4);
 err4=sqrt(sum(sum(D4.^2))/(K))
 
 D5=double(F5)-double(h5);
 err5=sqrt(sum(sum(D5.^2))/(K))
 
 D6=double(F6)-double(h6);
err6=sqrt(sum(sum(D6.^2))/(K))


 err=(err1+err2+err3+err4+err5+err6)/6;
 disp('RMSE averaged over all images=');
 disp(err);