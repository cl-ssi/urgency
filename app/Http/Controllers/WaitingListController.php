<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\WaitingList;

class WaitingListController extends Controller
{

    public function store(Request $request)
    {
        return WaitingList::create($request->all());
    }

}
