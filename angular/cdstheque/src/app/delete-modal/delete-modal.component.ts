import { Component, Input } from '@angular/core';
import { NgbActiveModal} from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-delete-modal',
  templateUrl: './delete-modal.component.html',
  styleUrls: ['./delete-modal.component.scss'],
  providers:[NgbActiveModal]
})
export class DeleteModalComponent {

  @Input() artist:string = '';

  constructor(public activeModal : NgbActiveModal){}

}
