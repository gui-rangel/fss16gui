# Feature Selection

##Datasets

<table>
<tr>
<td> Dataset </td>
<td> #Instances </td>
<td> #Attributes </td>
</tr>
<tr>
<td> breast-cancer </td>
<td> 286 </td>
<td> 9 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 958 </td>
<td> 9 </td>
</tr>
<tr>
<td> vote </td>
<td> 435 </td>
<td> 16 </td>
</tr>
<tr>
<td> ionosphere </td>
<td> 351 </td>
<td> 34 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 768 </td>
<td> 8 </td>
</tr>
<tr>
<td> iris </td>
<td> 150 </td>
<td> 4 </td>
</tr>
</table>

###Feature Selection using J48

<table>
<tr>
<td />
<td> #Features </td>
<td />
<td> Recall </td>
<td />
<td> Precision </td>
<td />
</tr>
<tr>
<td> Dataset </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
</tr>
<tr>
<td> breast-cancer </td>
<td> 9 </td>
<td> 3 </td>
<td> 0.778 </td>
<td> 0.756 </td>
<td> 0.836 </td>
<td> 0.925 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 9 </td>
<td> 2 </td>
<td> 0.887 </td>
<td> 0.885 </td>
<td> 0.878 </td>
<td> 0.707 </td>
</tr>
<tr>
<td> vote </td>
<td> 16 </td>
<td> 1 </td>
<td> 0.97 </td>
<td> 0.948 </td>
<td> 0.97 </td>
<td> 0.981 </td>
</tr>
<tr>
<td> ionosphere </td>
<td> 34 </td>
<td> 2 </td>
<td> 0.964 </td>
<td> 0.938 </td>
<td> 0.908 </td>
<td> 0.913 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 8 </td>
<td> 4 </td>
<td> 0.814 </td>
<td> 0.84 </td>
<td> 0.79 </td>
<td> 0.779 </td>
</tr>
<tr>
<td> iris </td>
<td> 4 </td>
<td> 1 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.887 </td>
</tr>
</table>

### Feature Selection using Wrapper

<table>
<tr>
<td />
<td> #Features </td>
<td />
<td> Recall </td>
<td />
<td> Precision </td>
<td />
</tr>
<tr>
<td> Dataset </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
</tr>
<tr>
<td> breast-cancer </td>
<td> 9 </td>
<td> 6 </td>
<td> 0.778 </td>
<td> 0.772 </td>
<td> 0.836 </td>
<td> 0.891 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 9 </td>
<td> 9 </td>
<td> 0.887 </td>
<td> 0.887 </td>
<td> 0.878 </td>
<td> 0.878 </td>
</tr>
<tr>
<td> vote </td>
<td> 16 </td>
<td> 1 </td>
<td> 0.97 </td>
<td> 0.948 </td>
<td> 0.97 </td>
<td> 0.981 </td>
</tr>
<tr>
<td> ionosphere </td>
<td> 34 </td>
<td> 2 </td>
<td> 0.964 </td>
<td> 0.987 </td>
<td> 0.908 </td>
<td> 0.925 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 8 </td>
<td> 4 </td>
<td> 0.814 </td>
<td> 0.842 </td>
<td> 0.79 </td>
<td> 0.797 </td>
</tr>
<tr>
<td> iris </td>
<td> 4 </td>
<td> 1 </td>
<td> 0.94 </td>
<td> 0.96 </td>
<td> 0.94 </td>
<td> 0.889 </td>
</tr>
</table>

###Feature Selection using CFS

<table>
<tr>
<td />
<td> #Features </td>
<td />
<td> Recall </td>
<td />
<td> Precision </td>
<td />
</tr>
<tr>
<td> Dataset </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
<td> All </td>
<td> Selected </td>
</tr>
<tr>
<td> breast-cancer </td>
<td> 9 </td>
<td> 2 </td>
<td> 0.778 </td>
<td> 0.764 </td>
<td> 0.836 </td>
<td> 0.935 </td>
</tr>
<tr>
<td> tic-tac-toe </td>
<td> 9 </td>
<td> 5 </td>
<td> 0.887 </td>
<td> 0.917 </td>
<td> 0.878 </td>
<td> 0.798 </td>
</tr>
<tr>
<td> vote </td>
<td> 16 </td>
<td> 5 </td>
<td> 0.97 </td>
<td> 0.963 </td>
<td> 0.97 </td>
<td> 0.963 </td>
</tr>
<tr>
<td> ionosphere </td>
<td> 34 </td>
<td> 2 </td>
<td> 0.964 </td>
<td> 0.938 </td>
<td> 0.908 </td>
<td> 0.913 </td>
</tr>
<tr>
<td> diabetes </td>
<td> 8 </td>
<td> 4 </td>
<td> 0.814 </td>
<td> 0.852 </td>
<td> 0.79 </td>
<td> 0.782 </td>
</tr>
<tr>
<td> iris </td>
<td> 4 </td>
<td> 2 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.94 </td>
<td> 0.887 </td>
</tr>
</table>
