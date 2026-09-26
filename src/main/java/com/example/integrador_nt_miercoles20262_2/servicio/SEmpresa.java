package com.example.integrador_nt_miercoles20262_2.servicio;

import com.example.integrador_nt_miercoles20262_2.modelo.MEmpresa;
import com.example.integrador_nt_miercoles20262_2.repositorio.IEmpresa;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class SEmpresa {

    private IEmpresa iEmpresa;

    public SEmpresa(IEmpresa iEmpresa) {
        this.iEmpresa = iEmpresa;
    }

    //Consulta de empresas
    public List<MEmpresa> consultaTodasLasEmpresas() throws Exception {
        try {
            return
                    this.iEmpresa.findAll();
        } catch (RuntimeException e) {
            throw new RuntimeException(e);
        }
    }
    //Consulta por ID
    public MEmpresa ConsultaPorId(UUID id){
        try{
            Optional<MEmpresa> empresaEncontrada = this.iEmpresa.findById(id);
            if(empresaEncontrada.isPresent()){
                return empresaEncontrada.get();
            }

        } catch (RuntimeException e) {
            throw new RuntimeException(e);
        }
    }
}

