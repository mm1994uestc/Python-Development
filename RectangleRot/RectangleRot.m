clear all;
close all;
clc
for IP=1:58
    I=imread(strcat('D:\PythonDevelopment\RectangleRot\Pic_In\',num2str(IP),'.png'));
    [row,clo,d]=size(I);
    T_L=row/3;
    T_H=row*2/3;
    x0=1; %row
    y0=1; %clo
    while(I(x0,y0,1)==0)
        if(x0>=(row-1))
            x0=1;
            y0=y0+1;
        end
        x0=x0+1;
    end
    if(x0>T_L && x0<T_H)
        I_Res=I;
    else
        if(x0>(row/2))
            x1=x0-300;
        else
            x1=x0+300;
        end
        y1=1;
        while(I(x1,y1,1)==0)
            y1=y1+1;
        end
        k=(y1-y0)/(x1-x0);
        Theta=-1*atan(k)*180/pi;
        I_Res=imrotate(I,Theta,'crop');
    end
    imwrite(I_Res,strcat('D:\PythonDevelopment\RectangleRot\Pic_Res\',[num2str(IP),'.png']));
end
