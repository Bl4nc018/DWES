package com.example.myothercatalog;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity { // Creamos la clase DetailActivity para que el botón funcione.

    private TextView nombre;
    private ImageView game;
    private TextView descripcion;

    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Ejercicio #3: Lo primero, es obtener el intent de la clase.
        Intent intent = getIntent();
        // Tras ello, creamos unas variables String que serán las que emplearemos para almacenar
        // los datos para el xml.
        String name = intent.getStringExtra("name");
        String description = intent.getStringExtra("descripcion");
        String url = intent.getStringExtra("image_url");
        // Seguidamente, con las variables TextView e ImageView que definiremos arriba como
        // private, las buscaremos en el layout de activity_detail por su id.
        nombre = findViewById(R.id.name);
        game = findViewById(R.id.imagen);
        descripcion = findViewById(R.id.descrip_game);
        // Y aquí ya modificaremos los TextView y el ImageView por los datos correctos que almacenamos
        // arriba.
        nombre.setText(name);
        Util.downloadBitmapToImageView(url, this.game);
        descripcion.setText(description);
    }
}
