package com.example.mycatalog;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.RelativeLayout;
import android.widget.TextView;

public class CatalogFragment extends Fragment {
    private Context context;

    // El siguiente método ayuda a crear una nueva instancia de CatalogFragment
    public static CatalogFragment newInstance() {
        CatalogFragment frag = new CatalogFragment();
        return frag;
    }

    // Este método a adjuntar el fragmento con la actividad.
    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
    }

    // El siguiente método crea y devuelve la vista (layout) del fragmento.
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {

    // Se infla el diseño del fragmento utilizando el LayoutInflater.

    // "Inflar el diseño" es el proceso de convertir un xml de diseño en objetos visuales reales para mostrar en la pantalla de la aplicación.

    // El tercer argumento "false" indica que no se debe adjuntar el diseño al contenedor "container" inmediatamente.
    // En su lugar, se infla solo para obtener una referencia a la vista del fragmento que se devolverá.

        View layout = inflater.inflate(R.layout.fragment_catalog, container, false);
        Button boton = layout.findViewById(R.id.navego);

        // Creamos un oyente para cuando hagamos clic en el botón.
        boton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Cuando se hace clic en el botón, inicia la actividad deseada.
                if (context != null) {
                    Intent myIntent = new Intent(context, DetailActivity.class);
                    context.startActivity(myIntent);
                }
            }
        });
        // Devolvemos la vista del fragmento con el botón y su oyente de clic.
        return layout;
    }
}
