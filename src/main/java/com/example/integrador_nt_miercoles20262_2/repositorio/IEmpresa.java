package com.example.integrador_nt_miercoles20262_2.repositorio;

import com.example.integrador_nt_miercoles20262_2.modelo.MEmpresa;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface IEmpresa extends JpaRepository<MEmpresa, UUID> {


    List<MEmpresa> findByNombre(String nombre);







}
