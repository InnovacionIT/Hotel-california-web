import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { RegistroRequest } from './registroRequest';

@Injectable({
  providedIn: 'root'
})
export class RegistroService {
  constructor(private http: HttpClient) { }
  private url = 'assets/clientes.json';

  getData(): Observable<any> {
    return this.http.get(this.url);
  }

  postData(data:RegistroRequest): Observable<any>  {
    return this.http.post<any>(this.url, data );
  }

}
