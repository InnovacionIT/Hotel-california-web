import { Component, OnInit } from '@angular/core';
import  { RegistroService } from '../../services/registro.service'
import { RegistroRequest } from 'src/app/services/registroRequest';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  ngOnInit(): void {
  }
  registro: RegistroRequest = {
    nombre: '',
    email: '',
    password: '',
    apellido: '',
    ciudad: '',
    fechaNacimiento: '',
    telefono: ''
  }

  constructor(private registroService: RegistroService) { }



  onSubmit() {
    console.log(this.registro); // Imprimir los datos en la consola

    this.registroService.getData()
    .subscribe(
      (response) => {
        console.log('Respuesta de la solicitud GET', response);
        // Se solicita todos los datos para corroborar si el usuario existe o no.
      },
      (error) => {
        console.log('Error en la solicitud GET', error);
        // Manejo de errores de la solicitud GET.
      }
    );

    this.registroService.postData(this.registro)
      .subscribe(
        (response) => {
          console.log('Solicitud POST exitosa', response);
          // Aquí puedes realizar acciones adicionales después de una solicitud exitosa
        },
        (error) => {
          console.log('Error en la solicitud POST', error);
          // manejar los errores de la solicitud
        }
      );






}
}
