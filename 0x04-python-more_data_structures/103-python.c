#include <stdio.h>
#include <Python.h>
/* [Dtechguru] */

/**
 * print_python_bytes - all information th ebytes caiies is printed out
 *
 * Author: [Dtechguru]
 * @p: Python Object
 * Return: should'nt return any thing here (Detechguru)
 */
void print_python_bytes(PyObject *p)/*return Null*/
{
	char *string;/* characters in a string adress*/
	long int size, i, limit;/*Do Hard thing's*/

	/* ok Cis is not fun */
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	/* trying to get use to inputing comments */
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);/*lets do hard things*/

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);/*Dtechguru*/
		else/*an else statent*/
			printf(" %02x", 256 + string[i]);

	/*a new line is to be printed [Dtechguru]*/
	printf("\n");
}

/**
 * print_python_lists - the information in list is printed
 *
 * Author: [{Dtechguru}]
 * @p: Python Obj
 * Return: dont bother returning
 */
void print_python_list(PyObject *p)
{
	/* long datatypes*/
	long int size, i;
	PyListObject *list;
	PyObject *obj;
/* lets determine the size of this di*\*/
	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
/* printf statement here almost used print(f) lol (Dtechguru)*/
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

/* create a for statement */
	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i]; /* Dtechguru */
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);/*Dtecguru*/
		if (PyBytes_Check(obj))
			print_python_bytes(obj);/*Dtechguru*/
	}
