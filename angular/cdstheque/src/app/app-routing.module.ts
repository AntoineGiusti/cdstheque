import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CdsComponent } from './cds/cds.component';
import { CdDetailComponent } from './cd-detail/cd-detail.component';


const routes: Routes = [
  { path: 'cds', component: CdsComponent},
  { path: 'detail/:id', component: CdDetailComponent },
  { path: '', redirectTo: '/', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

 }
