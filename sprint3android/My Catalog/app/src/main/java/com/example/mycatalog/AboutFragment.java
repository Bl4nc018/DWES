package com.example.mycatalog;

import android.os.Bundle;

import androidx.annotation.Nullable;
import androidx.annotation.StringRes;
import androidx.fragment.app.Fragment;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

public class AboutFragment extends Fragment {
    public static AboutFragment newInstance() {  // Creación de nueva instancia de AboutFragment
        AboutFragment frag = new AboutFragment();
        return frag;
    }

    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable
    Bundle savedInstanceState) { // Creación y devolución de la vista del fragmento
        View layout = inflater.inflate(R.layout.fragment_about, container, false);
        // Inflamos el diseño del fragmento en la vista del mismo.
        return layout;
    }
}
