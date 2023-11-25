package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class GameViewHolder extends RecyclerView.ViewHolder{
    // Aquí nos encontramos los elementos de la vista de la celda
    private TextView name;
    private ImageView game;
    private Button button;

    // Este constructor recibe la vista de la celda e inicializa los atributos con los elementos de la misma.
    public GameViewHolder(@NonNull View ivi) {
        super(ivi);
        name = ivi.findViewById(R.id.text_view_game);
        game = ivi.findViewById(R.id.image_view_game);

        // Ejercicio #2: Declaramos tanto la variable en private como en GameViewHolder, en donde
        // añadiremos una linea para encontrar en la vista el botón.
        button = ivi.findViewById(R.id.button);
    }
    // Y en este último método se muestran los datos en la vista de la celda:
    public void showData(GameData gameData) {
        name.setText(gameData.getName()); // Establecemos el nombre del juego en el TextView
        Util.downloadBitmapToImageView(gameData.getImage_url(), this.game); // Empleamos una utilidad para descargar y establecer la imagen del juego en el ImageView.

        // Ejercicio #2: Añadimos un OnClickListener para que al pulsar el botón obtenga el contexto,
        // cree un nuevo Intent con este el cual nos lleve hasta DetailActivity.
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Context context = v.getContext();
                Intent intent = new Intent(context, DetailActivity.class);
                // Ejercicio #3: Mediante el uso de intents, empleamos putExtra() que es una función que nos permite
                // añadir datos adicionales a un intent antes de iniciar un nuevo componente. get(TipoVariable)Extra() es lo que
                // nos permite recoger estos datos enviados.
                intent.putExtra("name", gameData.getName());
                intent.putExtra("descripcion", gameData.getDescripcion());
                intent.putExtra("image_url", gameData.getImage_url());
                context.startActivity(intent);
            }
        });
    }
}
