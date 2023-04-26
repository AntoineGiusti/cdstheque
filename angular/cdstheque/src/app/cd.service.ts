import { Injectable } from '@angular/core';
import { Cd } from "./cds/cd";
import { Observable, of } from 'rxjs';
import { MessagesService } from "../app/messages.service";
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { observableToBeFn } from 'rxjs/internal/testing/TestScheduler';


@Injectable({
  providedIn: 'root'
})
export class CdService {

  constructor(
    private http : HttpClient,
    private messageService : MessagesService

    ) {}

  private log(message: string){
    this.messageService.add(`cdService : ${message}`);
  }

  private cdsUrl = 'http://127.0.0.1:5000/cds';

  private handleError<T>(operation = 'operation', result?: T){
    return (error: any): Observable<T> => {
      console.error(error);
      this.log(`${operation} failed : ${error.message}`);
      return of(result as T);
    }
  }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type' : 'application/json' })
  };
  // GET cds from the server
  getCds(): Observable<Cd[]>{
      return this.http.get<Cd[]>(`${this.cdsUrl}`)
      .pipe(
        tap(_ => this.log('fetches cds')),
        catchError(this.handleError<Cd[]>('getCds', []))
      );
  }
  // GET cd by id from server
  getCd(id: number) : Observable<Cd>{
    const url = `${this.cdsUrl}/id/${id}`;
    return this.http.get<Cd>(url).pipe(
      tap(_ => this.log(`fetched cd id=${id}`)),
      catchError(this.handleError<Cd>(`getCd id=${id}`))
    );
  }
  // PUT: update the cd on the server
  updateCd(cd : Cd): Observable<any> {
    return this.http.put(`${this.cdsUrl}/id/${cd.id}`, cd, this.httpOptions).pipe(
      tap(_ => this.log(`updated cd id=${cd.id}`)),
      catchError(this.handleError<any>('updateCd'))
    );
  }
  //POST a new cd
  addCd(cd : Cd): Observable<Cd>{
    return this.http.post<Cd>(`${this.cdsUrl}/`, cd ,this.httpOptions).pipe(
      tap((newCd : Cd) => this.log(`added cd w/ id=${newCd.id}`)),
      catchError(this.handleError<Cd>('addCd'))
    );
  }

  //DELETE a cd
  deleteCd(id : number): Observable<Cd>{
    const url = `${this.cdsUrl}/id/${id}`;
    return this.http.delete<Cd>(url, this.httpOptions).pipe(
      tap(_ => this.log(`deleted cd id=${id}`)),
      catchError(this.handleError<Cd>('deleteCd'))
    )
  }

  //SEARCH cd
  searchCds(term:string): Observable<Cd[]>{
    if (!term.trim()){
      return of([]);
    }
    return this.http.get<Cd[]>(`${this.cdsUrl}/artist/${term}`).pipe(
      tap(x => x.length ?
        this.log(`nous avons trouver ceci pour "${term}"`) :
        this.log(`pas de cds pour trouvé pour "${term}"`)),
      catchError(this.handleError<Cd[]>('serarchCds'))
    );
  }


}
