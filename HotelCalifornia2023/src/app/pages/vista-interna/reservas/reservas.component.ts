import { Component, OnInit } from '@angular/core';
import { FacturaService } from 'src/app/services/factura.service';
import { Factura } from 'src/app/services/factura';
import { ReservacionService } from '../../../services/reservacion.service';

@Component({
  selector: 'app-reservas',
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent implements OnInit {
  constructor(
    private facturaService: FacturaService,
    private reservacionService: ReservacionService
    ) { }
  factura: any;
  habitacionId: number = 1; // Valor de ejemplo para habitacionId
  usuarioId: number = 1; // Valor de ejemplo para usuarioId
  reservaId: number = 1; // Valor de ejemplo para reservaId

   ngOnInit(): void {
     this.facturaService.Factura().subscribe((Factura) => {
      console.log(Factura);
     });
     this.facturaService.detalle().subscribe((detalle) => {
      console.log(detalle);
     });
     this.facturaService.detallePago().subscribe((detallePago) => {
      console.log(detallePago);
     });
     this.getListadoHabitaciones();
     this.getDetalleHabitacion(this.habitacionId);
     this.verificarDisponibilidad(this.habitacionId, new Date(), new Date());
     this.createReservation({ usuarioId: this.usuarioId, habitacionId: this.habitacionId, fechaReserva: new Date() });
     this.getReservaPorHabitacion(this.habitacionId);
     this.getReservaPorCliente(this.usuarioId);
     this.modificarReserva(this.reservaId, { usuarioId: this.usuarioId, habitacionId: this.habitacionId, fechaReserva: new Date() });
     this.getReservaPorId(this.reservaId);
     this.eliminarReserva(this.reservaId);
    }


     addFactura(){
      this.facturaService.addFactura(this.factura).subscribe((factura) => {
        console.log('factura'+ this.addFactura);
      })
     }

     addDetalle(){
      this.facturaService.addDetalle(this.factura).subscribe((detalle) => {
        console.log('detalle' + this.addDetalle)
      })
     }
     addDetallePago(){
      this.facturaService.addFactura(this.factura).subscribe((detallePago) => {
        console.log('detallePago'+ this.addDetallePago);
      })
     }
     addTipoPago(){
      this.facturaService.addFactura(this.factura).subscribe((tipoPago) => {
        console.log('detallePago'+ this.addTipoPago);
      })
     }

     getListadoHabitaciones(): void {
      this.reservacionService.getListadoHabitaciones().subscribe(habitaciones => {
        console.log('Listado de habitaciones:', habitaciones);
      });
    }

    getDetalleHabitacion(roomId: number): void {
      this.reservacionService.getDetalleHabitacion(roomId).subscribe(detalle => {
        console.log('Detalle de habitación:', detalle);
      });
    }

    getReservaPorId(reservationId: number): void {
      this.reservacionService.getReserva(reservationId).subscribe(reserva => {
        console.log('Reserva por ID:', reserva);
      });
    }

    getReservaPorHabitacion(roomId: number): void {
      this.reservacionService.getReservasPorHabitacion(roomId).subscribe(reservas => {
        console.log('Reservas por habitación:', reservas);
      });
    }

    getReservaPorCliente(clientId: number): void {
      this.reservacionService.getReservaPorCliente(clientId).subscribe(reservas => {
        console.log('Reservas por cliente:', reservas);
      });
    }

    modificarReserva(reservationId: number, updatedData: any): void {
      this.reservacionService.modificarReserva(reservationId, updatedData).subscribe(reserva => {
        console.log('Reserva modificada:', reserva);
      });
    }

    createReservation(reservationData: any): void {
      this.reservacionService.createReservation(reservationData).subscribe(reserva => {
        console.log('Reserva creada:', reserva);
      });
    }

    eliminarReserva(reservationId: number): void {
      this.reservacionService.eliminarReserva(reservationId).subscribe(() => {
        console.log('Reserva eliminada');
      });
    }

    verificarDisponibilidad(roomId: number, checkInDate: Date, checkOutDate: Date): void {
      this.reservacionService.verificarDisponibilidad(roomId, checkInDate, checkOutDate).subscribe(disponible => {
        console.log('Habitación disponible:', disponible);
      });
    }
    }
