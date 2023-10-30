package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

public class CatalogActivity extends AppCompatActivity {
    private Context context=this; // Recordamos la importancia de definir el contexto donde se ejecutan las apps para emplearlo más adelante.
    @Override
    protected void onCreate(Bundle savedInstanceState) { // Importante la creación de este método, que iniciará los widgets una vez se abra la app.
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog); // Establecemos la vista principal de una actividad basandonos en el .xml que creamos.
        Button boton = findViewById(R.id.navego); // Nos aseguramos de encontrar el botón que recién creamos.
        boton.setOnClickListener(new View.OnClickListener() { // Seteamos un controlador en el botón para comprobar cuando es clicado.
            @Override
            public void onClick(View view) { // Aqui, una vez se ejecute el click sobre el botón:
                Intent myIntent = new Intent(context, DetailActivity.class); // Instanciamos un intent para que, tras clickar en el botón se ejecute
                                                                             // la clase DetailActivity
                context.startActivity(myIntent);
            }

        });
    }
}