package com.example.myroomsocket;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.Point;
import android.graphics.Rect;
import android.graphics.RectF;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.os.Build;
import android.os.Bundle;
import android.util.Log;
import android.view.Display;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    Thread Thread1 = null;
    String SERVER_IP = "192.168.0.7";
    int SERVER_PORT = 12345;
//    char[] vals = new char[89];
    byte[] vals = new byte[1200];
    ImageView canvasView = null;
    Button btnStart;

    Bitmap tempBitmap;
    Canvas tempCanvas;

    Paint p;
    Paint pbase;

    TextView address;

//    @RequiresApi(api = Build.VERSION_CODES.O)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        canvasView = findViewById(R.id.imageView);

        btnStart = findViewById(R.id.btnStart);
        address = findViewById(R.id.txtIp);

        p = new Paint();
        p.setStrokeWidth(3);
        p.setColor(Color.rgb(0, 200, 0));

        pbase = new Paint();
        pbase.setStrokeWidth(10);

        Display display = getWindowManager().getDefaultDisplay();
        Point size = new Point();
        display.getSize(size);
        int width = size.x;
        int height = size.y;

        //Create a new image bitmap and attach a brand new canvas to it
        tempBitmap = Bitmap.createBitmap(width, height, Bitmap.Config.ARGB_8888);
        tempCanvas = new Canvas(tempBitmap);


        btnStart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                btnStart.setVisibility(View.INVISIBLE);
                address.setVisibility(View.INVISIBLE);
                canvasView.setVisibility(View.VISIBLE);

                SERVER_IP = address.getText().toString();
                Thread1 = new Thread(new Thread1());
                Thread1.start();
            }
        });


    }


    private InputStream input;

    class Thread1 implements Runnable {
        public void run() {
            Socket socket;
            Log.d("tagtag", "222");
            try {
                socket = new Socket(SERVER_IP, SERVER_PORT);
//                input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                input = socket.getInputStream();


                while(true) {
                    input.read(vals);
                    runOnUiThread(new Runnable() {

                        @Override
                        public void run() {
                            tempBitmap.eraseColor(Color.argb(50, 0, 0, 0));
                            Canvas tempCanvas = new Canvas(tempBitmap);

                            Path path = new Path();
                            Path path1 = new Path();
                            float lastX = 0;
                            float lastY = 0;

//                            float baseSegments = 12;
//                            float baseLineXi = tempCanvas.getWidth()*1.f/4.f;
//                            float baseLineYi = tempCanvas.getHeight()*1.f/2.f;
//                            float lastXBase = baseLineXi;
//                            float lastYBase = baseLineYi;
//                            float baseLineSegmentLength = (tempCanvas.getWidth()/2.f)/baseSegments;
//
                            for (int i = 0; i < vals.length; i++) {
//                                if(i<(int)baseSegments){
//                                        float baseX = baseLineXi+i*baseLineSegmentLength;
//                                        float baseY = baseLineYi+vals[i]/255.f*tempCanvas.getHeight()*1.f/4.f;
//                                        if(i==0){
//                                            path1.moveTo(baseX, baseY);
//                                        }else if(i==(int)baseSegments-1){
//                                            path1.lineTo(baseX, baseY);
//                                            path1.lineTo(baseX, baseLineYi);
//                                            path1.lineTo(baseLineXi, baseLineYi);
//                                        }else{
//                                            path1.quadTo(lastXBase, lastYBase, (float)(baseX+lastXBase)/2.f, (float)(baseY+lastYBase)/2.f);
//                                        }
////                                        pbase.setColor(Color.argb((int)((float)(vals[i])/255.f*200.f+50.f), vals[i], 255, 150));
//                                        tempCanvas.drawLine(baseLineXi+i*baseLineSegmentLength, baseLineYi, baseLineXi+i*baseLineSegmentLength+baseLineSegmentLength, baseLineYi, pbase);
//
//                                        lastXBase = baseX;
//                                        lastYBase = baseY;
//                                }

                                float x = ((float)(i)*(float)(tempCanvas.getWidth())/(float)(vals.length));

                                int val = (int)vals[i];
                                while(val<0)
                                    val+=255;

                                while(val>255)
                                    val-=255;

                                float y =  (float)(tempCanvas.getHeight()/2) - (float)((int)val-127)/254.f*(float)tempCanvas.getHeight()*.8f;//((float)((int)(vals[i]))/250.f)*2//(float)(tempCanvas.getHeight()/2)

                                tempCanvas.drawPoint(x, y, p);

//                                if(i==0) {
//                                    path.moveTo(0, (float) (tempCanvas.getHeight() / 2));
//                                }else if(i==vals.length-1) {
//                                    path.lineTo(x, y);
//                                    path.lineTo(x, tempCanvas.getHeight());
//                                    path.lineTo(-5, tempCanvas.getHeight());
//
//                                }else{
////                                    path.quadTo(lastX, lastY, (float)(x+lastX)/2.f, (float)(y+lastY)/2.f);
//                                    path.lineTo(x, y);
////                                    path.lineTo(x, tempCanvas.getHeight());
////                                    path.lineTo(-5, tempCanvas.getHeight());
//                                }


//                                lastX = x;
//                                lastY = y;
                            }

//                            path.setFillType(Path.FillType.INVERSE_EVEN_ODD);
//                            tempCanvas.drawPath(path, p);
//                            tempCanvas.drawPoint()
//                            tempCanvas.drawPath(path1, p);

//                            tempCanvas.drawLine(0,(float)(tempCanvas.getHeight()/2), tempCanvas.getWidth(), (float)(tempCanvas.getHeight()/2), p);
//                            tempCanvas.drawLine(0,(float)(tempCanvas.getHeight()/2+250), tempCanvas.getWidth(), (float)(tempCanvas.getHeight()/2+250), p);
                            //Attach the canvas to the ImageView
                            canvasView.setImageDrawable(new BitmapDrawable(getResources(), tempBitmap));
                        }
                    });
                }
            } catch (IOException e) {
                e.printStackTrace();
                Log.d("tagtag", "eee");

            }
        }
    }

//    public class SimpleDrawingView extends View {
//        // ...variables and setting up paint...
//        // Let's draw three circles
//        @Override
//        protected void onDraw(Canvas canvas) {
//            Paint drawPaint = new Paint();
//            drawPaint.setColor(Color.RED);
//            drawPaint.setAntiAlias(true);
//            drawPaint.setStrokeWidth(5);
//
//            canvas.drawCircle(50, 50, 20, drawPaint);
//            drawPaint.setColor(Color.GREEN);
//            canvas.drawCircle(50, 150, 20, drawPaint);
//            drawPaint.setColor(Color.BLUE);
//            canvas.drawCircle(50, 250, 20, drawPaint);
//        }
//    }


}
