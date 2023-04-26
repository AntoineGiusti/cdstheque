import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Cd } from './cds/cd';

@Injectable({
  providedIn: 'root'
})
export class InMemoryDataService implements InMemoryDbService {

  createDb(){
    const cds = [
      {id : 9, artist : "rolling stones", albume_name :"paint in black", year_published: "1971"},
      {id : 10, artist : "francis cabrel", albume_name :"petite marie", year_published: "1981"},
      {id : 11, artist : "indochine", albume_name :"paradize", year_published: "2001"},
      {id : 12, artist : "sum41", albume_name :"no killer, no filler", year_published: "1999"}
    ];
    return {cds};
  }

  genId(cds:Cd[]) : number {
    return cds.length > 0 ? Math.max(...cds.map(cd => cd.id)) + 1 : 11;
  }

}
