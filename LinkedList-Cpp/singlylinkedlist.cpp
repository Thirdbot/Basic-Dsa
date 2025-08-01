#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;

    Node() : data(0), next(nullptr) {}
    Node(int value) : data(value), next(nullptr) {}
};

class SinglyLinkedList {
    private:
        Node* head;
        SinglyLinkedList():head(nullptr) {}
    public:
        SinglyLinkedList(int value){
            head = new Node(value);
        }

        Node* typeConvert(){
            return head;
        }

        void add(int value) {
            Node* current = head;
            if (current->next == nullptr){
                current->next = new Node(value);
            }
            else{
                while(current->next != nullptr) {
                    current = current->next;
                }
                current->next = new Node(value);
            }
        }
        void traverse(){
            Node* current = head;
            while (current != nullptr) {
                cout << current->data << " -> ";
                current = current->next;
            }
            cout << "NULL" << endl;
            
        }

        void remove(int data){
            Node* current = head;
            while ( current->next != nullptr) {
                if (current->next->data == data){
                    current->next = current->next->next;
                    
                }
               current = current->next;
               
            }
        }
        void insertafter(int value, int afterValue){
            Node* current = head;
            Node* newNode = new Node(value);
            while (current != nullptr){
                if (current->data == afterValue){
                    newNode->next = current->next;
                    current->next = newNode;;
                }
                current = current->next;
            }
        }

};

int main() {
    SinglyLinkedList list(10);
    list.add(20);
    list.add(30);
    list.traverse(); // Output: 10 -> 20 -> 30 -> NULL
    list.remove(20);
    list.traverse(); // Output: 10 -> 30 -> NULL
    list.insertafter(25, 10);
    list.traverse(); // Output: 10 -> 25 -> 30 -> NULL
    return 0;
};